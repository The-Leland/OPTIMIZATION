


from sqlalchemy import select, join
from util.reflection import Product, Warranty, ProductCategoryXref, Category

def get_all_products():
    stmt = select(Product)
    products = session.execute(stmt).fetchall()

    results = []
    for row in products:
        product_dict = dict(row._mapping)

        
        warranty = session.execute(
            select(Warranty).where(Warranty.c.product_id == product_dict['product_id'])
        ).first()
        if warranty:
            product_dict["warranty"] = dict(warranty._mapping)

        
        category_joins = (
            select(Category.c.category_id, Category.c.category_name)
            .select_from(
                join(ProductCategoryXref, Category,
                     ProductCategoryXref.c.category_id == Category.c.category_id)
            )
            .where(ProductCategoryXref.c.product_id == product_dict['product_id'])
        )
        categories = session.execute(category_joins).fetchall()
        product_dict["categories"] = [dict(c._mapping) for c in categories]

        results.append(product_dict)

    return jsonify(results), 200
