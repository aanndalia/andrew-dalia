import web
import sqlite3
import HTML

web.config.debug = True

render = web.template.render('templates/')

urls = (
    '/', 'index', '/filter', 'filter'
)

# the lower limit for the market value filter is populated by the input form
lowerLimit = 0.0

class index:
    def GET(self):
        portfolioPositionsTable = renderMarketValuePositionsTable()
        return render.index(portfolioPositionsTable, lowerLimit)
        
class filter:
    def POST(self):
        global lowerLimit
        i = web.input()
        lowerLimit = i.marketValueLowerLimit if i.marketValueLowerLimit else 0.0
        raise web.seeother('/')

def getMarketValuePositionsView():
    """
    Queries the marketvalue positions view in the portfolios database
    and stores it as a list of lists
    
    :rtype: list
    """
    dbName = 'portfoliosdb.db'
    lowerLimitFilterSql = 'where marketvalue > %s' % lowerLimit 
    querySql = 'select * from marketvalue_positions_view %s' % lowerLimitFilterSql
    print "full query is", querySql
    allData = []
    try:
        con = sqlite3.connect(dbName)
        cur = con.cursor()
        cur.execute(querySql)
        allData = cur.fetchall()
    except sqlite3.Error, e:
        print "Error %s" % e.args[0]
    finally:
        if con:
            con.close()
            
    return allData
    
def renderMarketValuePositionsTable():
    """
    Gets market value positions data and renders it as an html table
    
    :rtype: str
    """
    table_data = getMarketValuePositionsView()
    headerRow = ['Portfolio',   'ISIN',   'Market Value']
    htmlcode = HTML.table(table_data, header_row=headerRow)
    return htmlcode
        

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()