##############################################################################################################
# Authors: Carlos Giralt Fuixench, David Jiménez Omeñaca                                                     #
# Date: 24-2-24                                                                                              #
# Subject: Algoritmia básica                                                                                 #
# Description: contains the definition and implementation of a class used to represent the variables of our  # 
# backtracking problem                                                                                       #
##############################################################################################################
from functools import reduce
import random
from src.article import Article


def file_to_variables(file_name):
    """
    Pre: file_name is the name of a file containing the size of a paper's page and a list of articles 
    with their corresponding origin coordinates and size.
    Post: returns a Variables object containing all the information extracted from file_name

    """

    with open(file_name, "r") as f:
        header = f.readline()
        variables = []

        while header:
            header = header[:-1]
            page_list = [int(_) for _ in header.split(" ")]
            page = Article((0, 0), page_list[2], page_list[1]).polygon
            n = page_list[0]

            list_art = []

            for _ in range(0, n):
                line = f.readline()[:-1]
                one_art_l = [int(_) for _ in line.split(" ")]
                list_art.append(Article((one_art_l[2], one_art_l[3]), one_art_l[1], one_art_l[0]))

            variables.append(Variables(list_art, n, page))
            header = f.readline()

        return variables


class Variables:
    """
    Definition and method implementation of a class that contains 
    all the variables involved in our backtracking problem

    """

    def __str__(self):
        """
        Pre: True
        Post: Returns a string representation of self

        """
        aux = "Articles: [ "
        for article in self.list_art:
            aux += f"<{article}>"
        aux += f" ]\nPage: {self.page}\nNumber of articles: {self.n}"
        return aux

    def __init__(self, list_art, n, page):
        """
        Each Variables object instance consists of a list of articles, the number of articles
        and a polygonal representation of an Article, which pretends to be the page in which the
        articles must be placed

        """
        self.list_art = list_art
        self.n = n
        self.page = page

    def to_svg(self):
        """
        Pre: True
        Post: Returns an svg path for a visual representation of the page with all the articles in it

        """

        const_white_color = "#FFFFFF"

        def random_color():
            color = '#'
            for _ in range(6):
                color += random.choice('0123456789ABCDEF')
            return color

        page_svg = self.page.svg(fill_color=const_white_color, opacity=0.1)
        arts_svg = []
        for art in self.list_art:
            arts_svg.append(art.to_svg(color=random_color(), opacity=0.5))

        return (page_svg + "\n" + "\n".join(arts_svg)).replace("stroke=\"#555555\"", "stroke=\"#000000\"")

    def write_svg(self, file_name):
        """
        Pre: file_name contains the name of a text file
        Post: Stores, in file_name, an svg path for a visual representation of the page with all the articles in it

        """
        with open(file_name, "w") as f:
            f.write(f'<svg version="1.1" xmlns="http://www.w3.org/2000/svg">\n')
            f.write(self.to_svg())
            f.write('</svg>')

    def article_fits(self, article_id, solution):
        """
        Pre: article_id contains the id of an article and solution contains our current solution
        Post: Returns true if and only if article_id fits in the article paper, given our
        current solution

        """

        if len(solution.indexes) == 0:
            return True
        else:
            article_pol = self.list_art[article_id].polygon
            articles_pol = [self.list_art[_].polygon for _ in solution.indexes]

            polygon = reduce(lambda x, y: x.union(y), articles_pol)

            return polygon.intersection(article_pol).area == 0

    def area_article(self, article_id):
        """
        Pre: article_id contains the id of an article
        Post: Returns the area of the polygonal representation of article_id

        """
        return self.list_art[article_id].area()

    def area_page(self):
        """
        Pre: True
        Post: Returns the area of the page in which we must place the articles

        """
        return self.page.area

    def sort_articles(self):
        def sort_key(element):
            return element.area()

        self.list_art.sort(key=sort_key)
