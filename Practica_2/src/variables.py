from shapely.geometry import Polygon
import random

const_white_color = "#FFFFFF"

def random_color():
    color = '#'
    for _ in range(6):
        color += random.choice('0123456789ABCDEF')
    return color

def get_union_vector(articles):
    if len(articles) == 0:
        return Polygon(((0,0),(0,0),(0,0),(0,0)))
    else:
        total_union = articles[0].polygon
        for article in articles[1:]:
            total_union = total_union.union(article.polygon)
        return total_union

def sum_without_intersections(articles, articles_not):
    total_union = get_union_vector(articles)
    return sum([article.intersection_area(total_union) for article in articles_not])


class Variables:
   
   ## funciona
    def __str__(self):
        aux = "Articles: [ "
        for article in self.list_art:
            aux += f"<{article}>"
        aux += f" ]\nPage: {self.page}\nNumber of articles: {self.n}"
        return aux
    
    ## funciona
    def __init__(self, list_art, n, page):
        self.list_art = list_art
        self.n = n
        self.page = page
    
    def to_svg(self):
        page_svg = self.page.svg(fill_color=const_white_color,opacity=0.1)
        arts_svg = []
        for art in self.list_art:
            arts_svg.append(art.to_svg(color=random_color(),opacity=0.5))

        return (page_svg + "\n" + "\n".join(arts_svg)).replace("stroke=\"#555555\"","stroke=\"#000000\"")
    
    def write_svg(self,file_name):
        with open(file_name,"w") as f:
            f.write(f'<svg version="1.1" xmlns="http://www.w3.org/2000/svg">\n')
            f.write(self.to_svg())
            f.write('</svg>')

    ## to be determined     
    def article_fits(self, article_id, solution):
        article = self.list_art[article_id]
        articles = [self.list_art[_] for _ in solution.indexes]
        return all([not one.intersects(article) for one in articles])
    
    def area_article(self, article_id):
        return self.list_art[article_id].area()
    
    def cote(self, solution):
        articles = [self.list_art[_] for _ in solution.indexes]
        articles_not = [self.list_art[i] for i in range(0,self.n) if i not in solution.indexes]
        return sum_without_intersections(articles, articles_not) + solution.totalArea
        
