import re

def slugify(product_name):
    slug=product_name.lower().strip()
    slug=re.sub(r"[^\w\s-]","",slug)
    slug = re.sub(r"[\s_-]+", "-", slug)
    slug = re.sub(r"^-+|-+$", "", slug)
    return slug