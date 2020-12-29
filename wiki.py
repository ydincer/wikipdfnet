import pdfkit

def wikix(url,filename):
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdfkit.from_url(url,filename, configuration=config)


wikix('https://www.youtube.com/watch?v=f1hAispAJ9c','ibo.pdf')