# Instructions :
# Create a class to handle paginated content in a website. A pagination is used to divide long lists of content in a series of pages.

# The Pagination class will accept 2 parameters:

# items (default: []): A list of contents to paginate.
# pageSize (default: 10): The amount of items to show in each page.
# So for example we could initialize our pagination like this:

# alphabetList = "abcdefghijklmnopqrstuvwxyz".split('')

# p = Pagination(alphabetList, 4)


# The Pagination class will have a few methods:

# getVisibleItems() : returns a list of items visible depending on the pageSize
# So for example we could use this method like this:

# p.getVisibleItems() 
# # ["a", "b", "c", "d"]
# You will have to implement various methods to go through the pages such as:
# prevPage()
# nextPage()
# firstPage()
# lastPage()
# goToPage(pageNum)

# Here’s a continuation of the example above using nextPage and lastPage:

# alphabetList = "abcdefghijklmnopqrstuvwxyz".split('')

# p = Pagination(alphabetList, 4)

# p.getVisibleItems() 
# # ["a", "b", "c", "d"]

# p.nextPage()

# p.getVisibleItems()
# # ["e", "f", "g", "h"]

# p.lastPage()

# p.getVisibleItems()
# # ["y", "z"]


# Notes

# The second argument (pageSize) could be a float, in that case just convert it to an int (this is also the case for the goToPage method)
# The methods used to change page should be chainable, so you can call them one after the other like this: p.nextPage().nextPage()
# Please set the p.totalPages and p.currentPage attributes to the appropriate number as there cannot be a page 0.
# If a page is outside of the totalPages attribute, then the goToPage method should go to the closest page to the number provided 
# (e.g. there are only 5 total pages, but p.goToPage(10) is given: the p.currentPage should be set to 5; if 0 or a negative number is given, p.currentPage should be set to 1).

class Pagination():
    def __init__(self, items = [], pagesize = 10):
        self.items = items
        self.pagesize = pagesize
        self.pages = {}
        pageslice = slice(pagesize)
        i=1
        while len(self.items) > 0:
            self.pages[i] = items[pageslice]
            del items[0:pagesize]
            i += 1
        self.currentPage = 1
        self.numberOfPages = len(self.pages)
    def getVisibleItems(self):
        print(self.pages[self.currentPage])

    def prevPage(self):
        self.currentPage -= 1
        if self.currentPage < 1:
            self.currentPage = 1

    def nextPage(self):
        self.currentPage += 1
        if self.currentPage > self.numberOfPages:
            self.currentPage = self.numberOfPages

    def firstPage(self):
        self.currentPage = 1

    def lastPage(self):
        self.currentPage = self.numberOfPages

    def goToPage(self, number):
        self.currentPage = number
        if self.currentPage > self.numberOfPages:
            self.currentPage = self.numberOfPages
        if self.currentPage < 1:
            self.currentPage = 1


alphabetList = [*'abcdefghijklmnopqrstuvwxyz']

p = Pagination(alphabetList, 5)
p.getVisibleItems()
p.nextPage()
p.getVisibleItems()
p.prevPage()
p.getVisibleItems()
p.lastPage()
p.getVisibleItems()
p.firstPage()
p.getVisibleItems()
p.goToPage(6)
p.getVisibleItems()