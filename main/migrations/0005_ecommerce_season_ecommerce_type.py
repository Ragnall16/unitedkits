# Generated by Django 5.1.1 on 2024-09-16 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_ecommerce_sold_ecommerce_size_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ecommerce',
            name='season',
            field=models.CharField(choices=[('92/93', '92/93'), ('93/94', '93/94'), ('94/95', '94/95'), ('95/96', '95/96'), ('96/97', '96/97'), ('97/98', '97/98'), ('98/99', '98/99'), ('99/00', '99/00'), ('00/01', '00/01'), ('01/02', '01/02'), ('02/03', '02/03'), ('03/04', '03/04'), ('04/05', '04/05'), ('05/06', '05/06'), ('06/07', '06/07'), ('07/08', '07/08'), ('08/09', '08/09'), ('09/10', '09/10'), ('10/11', '10/11'), ('11/12', '11/12'), ('12/13', '12/13'), ('13/14', '13/14'), ('14/15', '14/15'), ('15/16', '15/16'), ('16/17', '16/17'), ('17/18', '17/18'), ('18/19', '18/19'), ('19/20', '19/20'), ('20/21', '20/21'), ('21/22', '21/22'), ('22/23', '22/23'), ('23/24', '23/24'), ('24/25', '24/25')], default='24/25', max_length=5),
        ),
        migrations.AddField(
            model_name='ecommerce',
            name='type',
            field=models.CharField(choices=[('home', 'Home'), ('away', 'Away'), ('third', 'Third')], default='home', max_length=5),
        ),
    ]