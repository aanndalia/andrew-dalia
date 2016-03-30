import sqlite3

def loadDataFromFile(filePath):
    """
    Load the portfolio positions data from a flat 
    file. Assume csv format
    
    :param filePath: the path to the file
    :type filePath: str
    
    :rtype: list
    """
    if not filePath:
        return []
    
    data = []    
    with open(filePath) as f:
        for line in f:
            data.append(tuple(line.strip().split(',')))
    return data

def executeSqlUpdates(fileData, con, sql):
    """
    Populate the portfoliodb database with the data
    from the file. This wil handle populating the given
    tableName.
    
    :param dataFromFile: The data coming from a file
    :type dataFromFile: list
    :param con: The database connection object
    :type con: sqlite db connection object
    :param tableName: The name of the table to insert into
    :type tableName: str
    """
    if not fileData or not con:
        return
    
    for tradeData in fileData: 
        print "sql", sql
        print "tradeData", tradeData
        resolvedSql = sql % tradeData
        print "Executing: %s" % resolvedSql
        con.execute(resolvedSql)
        
    con.commit()
    print "All records committed successfully"
    

def main():
    dbName = 'portfoliosdb.db'
    fullPathToDb = dbName
    securitiesFileLocation = 'securitiesfile.csv'
    tradesFileLocation = 'tradesfile.csv'
    securitiesData = loadDataFromFile(securitiesFileLocation)
    tradesData = loadDataFromFile(tradesFileLocation)
    insertTradeSql = "insert into trades (tradeid, isin, buyer, amount, portfolioname) values (%s,'%s', %s, %s, '%s')"    
    insertSecuritySql = "insert into securities (isin, multiplier, price) values ('%s', %s, %s)"    
    try:
        con = sqlite3.connect(fullPathToDb)
        executeSqlUpdates(securitiesData, con, insertSecuritySql)
        executeSqlUpdates(tradesData, con, insertTradeSql)
    except sqlite3.Error, e:
        print "Error %s" % e.args[0]
    finally:
        if con:
            con.close()

main()
