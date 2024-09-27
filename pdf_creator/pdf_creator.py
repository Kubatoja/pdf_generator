import asyncio
from playwright.async_api import async_playwright
from .style import *



async def html_to_pdf(output_path, data):
    
    city = data['city']
    date = data['date']
    order_No = data['order_No']
    course_No = data["course_No"]
    route = data["route"]
    loadings = data["loadings"]
    unloadings = data["unloadings"]
    comments = data["comments"]
    price = data["price"]
    currency = data["currency"]
    driver = data["driver"]
    carrier_details = data["carrier_details"]
    ordering_person_details = data["ordering_person_details"]
    route_documents = data["route_documents"]

    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>PDF</title>
        '''+style+'''
    </head>
    <body>
        <div class="pdf-container">
            <div class="first--section">
                <div class="company">
                    <h1>Company name</h1>
                    10-000 Rzeszów<br>
                    ul. Super 12 <br>
                    NIP 123456789<br>
                    tel. (11) 12 34 567<br>
                    <a href="www.yourpage.pl">www.yourpage.pl</a>
                </div>
                <div class="date">'''+city+''', '''+date+'''</div>
            </div>
            <div class="second--section"><h1>Zlecenie nr: '''+order_No+'''</h1>dotyczy kursu: '''+course_No+''' </div>
            <hr>
            <div class="third--section">
                <div class="third--section--left">
                    <div class="table--title">Trasa</div>
                    <div class="table--body">
                        '''+route+'''
                    </div>

                </div>
                <div class="third--section--right">
                    <div class="table">
                        <div class="table--title">Załadunki</div>
                        <div class="table--body">
                            '''+loadings+'''
                        </div>
                    </div>

                    <div class="table" id="unloadings">
                        <div class="table--title">Rozładunki</div>
                        <div class="table--body">
                            '''+unloadings+'''
                        </div>
                    </div>

                </div>
            </div>
            <hr>
            <div class="fourth--section">
                <div class="table--title"> Uwagi</div>
                <div class="table--body">'''+comments+'''</div>
            </div>
            <div class="fifth--section">
                <div class="fifth--left">
                    <div class="fifth--table--title"> 
                        Uzgodniona cena frachtu
                    </div>
                    <div class="fifth--table--body">
                        '''+price+" "+currency+'''
                    </div>
                </div>
                <div class="fifth--right">
                    <div class="fifth--table--title"> 
                        Kierowca
                    </div>
                    <div class="fifth--table--body">
                        '''+driver+'''
                    </div>
                </div>

            </div>
            <div class="sixth--section">
                <div class="sixth--left">
                    <div class="table--title">Dane przewoźnika</div>
                    <div class="table--body">
                        '''+carrier_details+'''
                    </div>
                </div>
                <div class="sixth--right">
                    <div class="table--title">Dane osoby zlecającej</div>
                    <div class="table--body">
                        '''+ordering_person_details+'''
                    </div>
                </div>

            </div>
            <div class="seventh--section">
                <div class="table--title">Dokumenty z kursu / trasy</div>
                    <div class="table--body">
                        '''+route_documents+'''
                    </div>
            </div>
            <hr>
            <div class="eight--section">
                <div class="table--title">Warunki przewozu</div>
                    <div class="table--body">
                        <p>Umowa przewozu, której dotyczy niniejsze zlecenie, jest zawierana na następujących warunkach:</p>
                    <p>1. W ramach umowy przewozu przewoźnik będzie zobowiązany do dostarczenia zleceniodawcy, niezwłocznie po
                    wykonaniu przewozu, wszystkich potwierdzonych dokumentów związanych z przewiezionymi rzeczami i
                    wykonanym przewozem, w szczególności faktury. Z tytułu tych czynności przewoźnikowi nie będzie przysługiwać
                    dodatkowe wynagrodzenie, jak również nie może on żądać zwrotu związanych z tymi czynnościami wydatków</p>
                    <p>2. Przewoźne płatne będzie w terminie 30 dni (płatne tylko w czwartki) od dnia doręczenia zleceniodawcy przez
                    przewoźnika prawidłowej faktury, która zostanie wystawiona po wykonaniu przez przewoźnika przewozu i
                    dostarczeniu zleceniodawcy razem z kompletem dokumentów, o których mowa w pkt. 1.
                    <b>Za potwierdzony dokument dostawy uważany jest wyłącznie oryginał dokumentu zawierającego
                    pokwitowanie odbioru ( czytelny podpis osoby umocowanej do dokonania odbioru towaru wraz
                    z pieczątką firmową oraz wskazanie daty odbioru ).</b></p>
                <p>3. Wszelkie Państwa wierzytelności wynikające z przyjęcia niniejszego zlecenia (z uwzględnieniem ewentualnych
                    przyszłych zmian) , w szczególności o zapłatę ceny, należności ubocznych lub wierzytelności odszkodowawcze,
                    nie mogą być, bez naszej pisemnej zgody, przedmiotem skutecznego przelewu (cesji) lub jakiegokolwiek
                    ograniczonego prawa rzeczowego ( w szczególności zastawu).</p>
                    </div>
            </div>
        </div>
    </body>
    </html>
    '''

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.set_content(html_content)
        await page.pdf(path=output_path, print_background=True)
        await browser.close()


def create_pdf(name, data):
    output_path = './pdf_storage/'+name+'.pdf'
    asyncio.run(html_to_pdf(output_path=output_path, data=data))