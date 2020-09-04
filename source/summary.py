from pathlib import Path

import pandas as pd


def verticale_summary(summary_lijst, mes, paduit, ordernummer, aantal_vdps):
    gesplitste_lijst_sum = []
    begin = 0
    eind = mes
    for index in range(aantal_vdps):
        gesplitste_lijst_sum.append(summary_lijst[begin:eind])
        begin += mes
        eind += mes

    print(gesplitste_lijst_sum)


    sum_lijst_vert = []
    count = 0

    # _______________________________________________________
    # _______________________________________________________

    for naam in summary_lijst:
        df = f'df{count}'
        print(df)
        df = pd.read_csv(f'tmp/{naam}', ",", encoding="utf-8", dtype="str")
        # todo maak een try except versie om de komma kolon optevangen
        #     df2 = pd.DataFrame([[f'{ordernummer}_baan_{count+1}']], dtype="str")
        df2 = pd.DataFrame([[f'{ordernummer}_baan_{count + 1} | {df.aantal.astype(int).sum()} etiketten']])  # dtype="int"
        print(df.aantal.astype(int).sum())

        sum_lijst_vert.append(df2)
        sum_lijst_vert.append(df)

        count += 1

        file_will_be_placed_in = Path(paduit.joinpath(f"{ordernummer}_v_sum.csv"))
        sam2 = pd.concat(sum_lijst_vert, axis=0).to_csv(file_will_be_placed_in, ";")

    return True

def html_sum_form_writer(titel, **kwargs):
    """"build a html file for summary purposes with  *kwargv
    search jinja and flask
    # todo css link toevoegen
    """
    # for key, value in kwargs.items():
    #     print(key, value)

    naam_html_file = f'result/{titel}_summary.html'
    with open(naam_html_file, "w") as f_html:
        #         for key, value in kwargs.items():
        #             print(key, value)

        print("<!DOCTYPE html>\n", file=f_html)
        print('<html lang = "en">\n', file=f_html)
        print("     <head>\n", file=f_html)
        print("<meta charset='UTF-8>'\n", file=f_html)
        print(f"<title>{titel.capitalize()}</title>\n", file=f_html)
        print("     </head>", file=f_html)
        print("         <body>", file=f_html)
        for key, value in kwargs.items():
            print(f' <p><b>{key}</b> : {value}<p/>', file=f_html)

        print("         </body>", file=f_html)
        print(" </html>", file=f_html)

    return naam_html_file

# todo summary banen invoegen

def summary_file(pad, order_num, *args):

    summary_values_from_arg = []
    for arg in args:
        summary_values_from_arg.append(arg)

    sum_filename_out = f'{order_num}_sum.txt'

    pad_en_file = Path(pad).joinpath(sum_filename_out)

    with open(pad_en_file, 'w', encoding='utf-8') as summary:
        print(f'ordernummer: {order_num}', file=summary)
        print(f'aantal gemaakte vdp\'s = {summary_values_from_arg[8]}')
        print(f'gebruikte csv file = {summary_values_from_arg[6]}', file=summary)
        print("_" * 50, file=summary)

        print(
            f'totaal van lijst is {summary_values_from_arg[2]} en het gemiddelde over {summary_values_from_arg[8] * summary_values_from_arg[0]} banen is {summary_values_from_arg[3]}',
            file=summary)
        print(f'afwijking over het gemiddelde: {summary_values_from_arg[4]}', file=summary)
        print("_" * 50, file=summary)


        print(f'mes: {summary_values_from_arg[0]}', file=summary)
        print(f'aantal rollen : {summary_values_from_arg[1]} : zie excel print voor rol specificaties', file=summary)
        # print(f'totaal: {summary_values_from_arg[2]}', file = summary)
        # print(f'gemiddelde: {summary_values_from_arg[3]}', file = summary)
        print(f'wikkel = {summary_values_from_arg[9]} etiket(ten)', file=summary)
        print(f'extra etiketten per rol = {summary_values_from_arg[10]}', file=summary)

        print(f'inloop en uitloop: {summary_values_from_arg[5]}', file=summary)
        print(f"Y waarde = {summary_values_from_arg[7]}", file=summary)
        print("_" * 50, file=summary)

        print("aantal staat voor en na elke rol op sluit etiket", file=summary)

    return len(summary_values_from_arg)


