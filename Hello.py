from flask import Flask, redirect, url_for,render_template
import pandas as pd
app = Flask(__name__)


def read_data():
    list_columns=["Year","Local_Time","UTC_Time","Magnitude","Location","Depth","Latitude","Longitude","Event_type","Assessment","Agency"]
    df=pd.DataFrame(columns=list_columns)
    count=100
    Magn_Max=3
    for i in range(1,6):
        url_i="http://www.seismo.ethz.ch/earthquakes/switzerland/all-earthquakes/index.html?tableA.Lokalzeit.filterOnlyNull=f&tableA.UTC-Zeit.filterOnlyNull=f&tableA.Ort.filterOnlyNull=f&tableA.Tiefe.filterOnlyNull=f&tableA.Breite.filterOnlyNull=f&tableA.L%C3%A4nge.filterOnlyNull=f&tableA.Ereignis-Typ.filterOnlyNull=f&tableA.Auswertung.filterOnlyNull=f&tableA.Dienst.filterOnlyNull=f&tableA.Magnitude.filterComparator=ge&tableA.Magnitude.filterValue1="+str(Magn_Max)+"&tableA.Magnitude.filterOnlyNull=f&createFilter=Filter+anwenden&tableA.page="+str(i)+"&tableA.records="+str(count)+"#tableA-anchor"
        df_i=pd.read_html(url_i)
        df_i=pd.DataFrame(df_i[0])
        df_i.columns=list_columns
        df=pd.concat([df,df_i])

    df=df[df['Magnitude']>0]
    return(df)


# Home page
@app.route('/')
def hello_world():
    data=read_data()
    return render_template('hello.html',data=data[:50].values)
    # return render_template('hello.html',data=[data.to_html(classes='data')],titles=data.columns.values)


if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug = True)