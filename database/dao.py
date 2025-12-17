from database.DB_connect import DBConnect
from model.gene import Gene
from model.interazione import Interazione
from model.localizzazione import Localizzazione


class DAO:
    @staticmethod
    def search_all_gene():
        DB = DBConnect.get_connection()
        cursor = DB.cursor(dictionary=True)
        cursor.execute("SELECT * FROM gene")
        result = {}
        for row in cursor:
            gene = Gene(**row)
            result[gene.id] = gene

        cursor.close()
        DB.close()

        return result

    @staticmethod
    def search_all_localization():
        DB = DBConnect.get_connection()
        cursor = DB.cursor(dictionary=True)
        cursor.execute("SELECT * FROM classificazione")
        result = []
        for row in cursor:
            gene = Localizzazione(**row)
            result.append(gene)

        cursor.close()
        DB.close()
        return result
    @staticmethod
    def search_connessioni(dizionario_geni):
        DB = DBConnect.get_connection()
        cursor = DB.cursor(dictionary=True)
        cursor.execute("SELECT * FROM interazione")
        result = {}
        dizionario_connessioni={}
        try:
            for row in cursor:
                connessione = Interazione(**row)
                gene1=dizionario_geni[connessione.id_gene1]
                gene2=dizionario_geni[connessione.id_gene2]
                if (gene1, gene2) in result:
                    if dizionario_connessioni[(gene1, gene2)]==connessione.correlazione:
                        pass
                    else:

                        result[(gene1, gene2)] = result[(gene1, gene2)] + connessione.correlazione
                        print(result[(gene1, gene2)])
                else:
                    result[(gene1, gene2)] = connessione.correlazione
                    dizionario_connessioni[(gene1, gene2)] = connessione.correlazione
            cursor.close()
            DB.close()
        except KeyError:
            pass



        return result

