# Generated by Django 4.0.6 on 2022-08-16 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicemgt', '0002_alter_invoice_invoice_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='line_eight',
            field=models.CharField(blank=True, default='', max_length=120, null=True, verbose_name='Line 3'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='line_eight_quantity',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Quantity'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='line_eight_total_price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Line Total (D)'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='line_eight_unit_price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Unit Price (D)'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='line_nine',
            field=models.CharField(blank=True, default='', max_length=120, null=True, verbose_name='Line 4'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='line_nine_quantity',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Quantity'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='line_nine_total_price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Line Total (D)'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='line_nine_unit_price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Unit Price (D)'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='line_seven',
            field=models.CharField(blank=True, default='', max_length=120, null=True, verbose_name='Line 2'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='line_seven_quantity',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Quantity'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='line_seven_total_price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Line Total (D)'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='line_seven_unit_price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Unit Price (D)'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='line_six',
            field=models.CharField(blank=True, default='', max_length=120, null=True, verbose_name='Line 1'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='line_six_quantity',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Quantity'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='line_six_total_price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Line Total (D)'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='line_six_unit_price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Unit Price (D)'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='line_ten',
            field=models.CharField(blank=True, default='', max_length=120, null=True, verbose_name='Line 5'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='line_ten_quantity',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Quantity'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='line_ten_total_price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Line Total (D)'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='line_ten_unit_price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Unit Price (D)'),
        ),
    ]
