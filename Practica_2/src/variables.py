from functools import reduce
import random

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
        
        const_white_color = "#FFFFFF"
        def random_color():
            color = '#'
            for _ in range(6):
                color += random.choice('0123456789ABCDEF')
            return color

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
        
        if len(solution.indexes)==0:
            return True
        else:    
            article_pol = self.list_art[article_id].polygon
            articles_pol = [self.list_art[_].polygon for _ in solution.indexes]
            
            polygon = reduce(lambda x,y:x.union(y),articles_pol)
            
            return polygon.intersection(article_pol).area == 0
    
    def area_article(self, article_id):
        return self.list_art[article_id].area()
    
    def cote(self, solution):
        articles_not_pol = [self.list_art[i].polygon for i in range(0,self.n) if (i not in solution.indexes and self.article_fits(i,solution))]
        
        return 0 if len(articles_not_pol) == 0 else reduce(lambda x,y:x.union(y),articles_not_pol).area + solution.totalArea
        
