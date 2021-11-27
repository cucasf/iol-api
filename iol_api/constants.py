class Mercado:
    BCBA = 'bCBA'
    NYSE = 'nYSE'
    NASDAQ = 'nASDAQ'
    AMEX = 'aMEX'
    BCS = 'bCS'
    ROFX = 'rOFX'

class Pais:
    ARG = 'argentina'
    USA = 'estados_Unidos'

class Instrumento:
    class ARG:
        ACCIONES = "Acciones"
        BONOS = "Bonos"
        OPCIONES = "Opciones"
        CAUCIONES = "Cauciones"
        FUTUROS = "Futuros"
        FCI = "FCI"

    class USA:
        ACCIONES = "Acciones"
        BONOS = "Bonos"
        ETFS = "Etfs"
        MONEDAS = "Monedas"

class Panel:
    
    class ARG:
        
        class ACCIONES:
            MERVAL = "Merval"
            PANEL_GENERAL = "Panel General"
            MERVAL_25 = "Merval 25"
            MERVAL_ARGENTINA = "Merval Argentina"
            BURCAP = "Burcap"
            CEDEARS = "CEDEARs"

        class BONOS:
           SOBERANO_ARS_CER = "Soberanos en pesos más Cer"
           SOBERANO_ARS_TF = "Soberanos en pesos a tasa variable"
           SOBERANO_ARS_TV = "Soberanos en pesos a tasa fija"
           SOBERANO_USD = "Soberanos en dólares"
           SOBERANO_USD_LINKED = "Soberanos dolar linked"
           PROVINCIALES_ARS = "Provinciales en pesos"
           PROVINCIALES_USD_LINKED = "Provinciales dolar linked"
           PROVINCIALES_USD = "Provinciales en dólares"
           PROVINCIALES_EUR = "Provinciales en euros"
           CUPONES_PBI = "Cupones vinculados al PBI"
           CORPORATIVOS_ARS = "Bonos corporativos en pesos"
           CORPORATIVOS_USD = "Bonos corporativos en dólares"
        
        class OPCIONES:
            ACCIONES = "De Acciones"
            BONOS = "De Bonos"
            CEDEARS = "De Cedears"
            ITM = "In-the-Money"
            OTM = "Out-the-Money"
            CALLS = "Calls"
            PUTS = "Puts"

        class FUTUROS:
            TODOS = "Todos"
            USD = "Dólar USA"
            MERVAL = "MERVAL"
            BONAR_X = "BONAR X"
            BONAR_2024 = "BONAR 2024"
            DICA = "DICA"
            CUPON_PBI = "Cupón PBI"
            ORO = "Oro"
            WTI = "Petróleo WTI"
            SOJA_CHICAGO = "Soja Chicago"
            INDICE_SOJA_ROSAFE = "Indice Soja Rosafé"
            SOJA = "Soja"
            MAIZ_CHICAGO = "Maíz Chicago"
            MAIZ = "Maíz"
            TRIGO = "Trigo"
        
        class FCI:
            TODOS = "Todos"
            PLAZOS_FIJOS_ARS = "Plazos Fijos Pesos"
            PLAZOS_FIJOS_USD = "Plazos Fijos Dólares"
            RENTA_FIJA_ARS = "Renta Fija Pesos"
            RENTA_FIJA_USD = "Renta Fija Dólares"
            RENTA_MIXTA_ARS = "Renta Mixta Pesos"
            RENTA_MIXTA_USD = "Renta Mixta Dólares"
            RENTA_VARIABLE_ARS = "Renta Variable Pesos"
            RENTA_VARIABLE_USD = "Renta Variable Dólares"

    class USA:
        class BONOS:
           SOBERANO_ARS_CER = "Soberanos en pesos más Cer"
           SOBERANO_ARS_TF = "Soberanos en pesos a tasa variable"
           SOBERANO_ARS_TV = "Soberanos en pesos a tasa fija"
           SOBERANO_USD = "Soberanos en dólares"
           SOBERANO_USD_LINKED = "Soberanos dolar linked"
           PROVINCIALES_ARS = "Provinciales en pesos"
           PROVINCIALES_USD_LINKED = "Provinciales dolar linked"
           PROVINCIALES_USD = "Provinciales en dólares"
           PROVINCIALES_EUR = "Provinciales en euros"
           CUPONES_PBI = "Cupones vinculados al PBI"
           CORPORATIVOS_ARS = "Bonos corporativos en pesos"
           CORPORATIVOS_USD = "Bonos corporativos en dólares"

class Ajustada:
    AJUSTADA = "ajustada"
    SIN_AJUSTAR = "sinAjustar"

class Plazo:
    T0 = 't0'
    T1 = 't1'
    T2 = 't2'

class Administradora:
    CONVEXITY = "CONVEXITY"
    SUPERVIELLE = "SUPERVIELLE"
    # ALLARIA = "Allaria"
    # ALLIANCE_BERNSTEIN = "ALLIANCE BERNSTEIN"

class TipoFondo:
    PLAZO_FIJO_PESOS = "plazo_fijo_pesos"
    RENTA_FIJA_PESOS = "renta_fija_pesos"
    RENTA_MIXTA_PESOS = "renta_mixta_pesos"
    RENTA_VARIABLE_PESOS = "renta_variable_pesos"
    PLAZO_FIJO_DOLARES = "plazo_fijo_dolares"
    RENTA_FIJA_DOLARES = "renta_fija_dolares"
    RENTA_MIXTA_DOLARES = "renta_mixta_dolares"
    RENTA_VARIABLE_DOLARES = "renta_variable_dolares"

class TipoDeOrden:
    PRECIO_LIMITE ='precioLimite'
    PRECIO_MERCADO ='precioMercado'

class Tarifas:
    GOLD = 0.005
    PLATINUM = 0.003
    BLACK = 0.001