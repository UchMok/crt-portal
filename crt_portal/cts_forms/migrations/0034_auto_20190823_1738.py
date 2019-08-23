# Generated by Django 2.2.4 on 2019-08-23 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cts_forms', '0033_auto_20190821_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='place',
            field=models.CharField(choices=[('home,', 'Home, potential home, or services to help with purchasing a home (banks, lenders, or other financial services)'), ('workplace', 'Workplace or potential workplace'), ('school', 'Educational institution (school, university), education program or educational activity (after school program or workshop)'), ('place_of_worship', 'Place of worship'), ('store', 'Retail/commercial building (store, restaurant, hotel, nightclub, theater, gym, or other commercial space)'), ('public_space', 'Outdoor public space (including car, street, sidewalk, park)'), ('voting', 'Voting location or ballot (including mail-in ballots)'), ('healthcare', 'Healthcare facility (including mental health or long-term care)'), ('incarcerated', 'Prison, jail, or juvenile corrections facility, or while otherwise incarcerated'), ('government_building', 'Another government building (courthouse, DMV, post office)')], default=None, max_length=100),
        ),
    ]