import psycopg 
def get_connection(): 
        return psycopg.connect(
                        dbname="market_intelligence",
                        user="syedrafiuddinaaqib",
        )