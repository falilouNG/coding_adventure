# Generated by Django 2.0.5 on 2018-08-29 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenericExpense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('date_expired', models.DateField()),
                ('final_value', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('is_paid', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': '7. Generic Expenses',
                'ordering': ['-date_expired'],
            },
        ),
        migrations.CreateModel(
            name='GenericExpenseCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
            ],
            options={
                'verbose_name_plural': '6. Expense Category',
            },
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'verbose_name_plural': '0. Payment Method',
            },
        ),
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('date_expired', models.DateField()),
                ('final_value', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('is_paid', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': '5. Payroll',
                'ordering': ['-date_expired'],
            },
        ),
        migrations.CreateModel(
            name='PayrollCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
            ],
            options={
                'verbose_name_plural': '3. Payroll Category',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True)),
                ('occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
            ],
            options={
                'verbose_name_plural': '4. Persons',
            },
        ),
        migrations.AlterModelOptions(
            name='bill',
            options={'ordering': ['-date_expired'], 'verbose_name_plural': '2. Bills'},
        ),
        migrations.AlterModelOptions(
            name='billcategory',
            options={'verbose_name_plural': '1. Bill Category'},
        ),
        migrations.AlterField(
            model_name='bill',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='payroll',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_payroll', to='expenses.PayrollCategory'),
        ),
        migrations.AddField(
            model_name='payroll',
            name='payment_method',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='expenses.PaymentMethod'),
        ),
        migrations.AddField(
            model_name='payroll',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='person_payroll', to='expenses.Person'),
        ),
        migrations.AddField(
            model_name='genericexpense',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_expenses', to='expenses.GenericExpenseCategory'),
        ),
        migrations.AddField(
            model_name='genericexpense',
            name='payment_method',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='expenses.PaymentMethod'),
        ),
        migrations.AddField(
            model_name='bill',
            name='payment_method',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='expenses.PaymentMethod'),
        ),
    ]
