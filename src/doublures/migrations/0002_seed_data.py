from django.db import migrations

DOUBLURES = [
    ("Christopher", "Cook"),
    ("Donna", "Hill"),
    ("George", "Price"),
    ("Michael", "Long"),
    ("Karen", "Foster"),
    ("Jacob", "Rogers"),
    ("Jessica", "Gray"),
    ("Jennifer", "Patel"),
    ("Brandon", "Bryant"),
    ("Jessica", "Hughes"),
    ("David", "Long"),
    ("Samuel", "Green"),
    ("Larry", "Foster"),
    ("Donna", "Roberts"),
    ("Eric", "Flores"),
    ("Nicole", "Murphy"),
    ("Ruth", "Clark"),
    ("Nicole", "Lopez"),
    ("Karen", "Bennett"),
    ("Brian", "Young"),
    ("Stephanie", "Bryant"),
    ("Janet", "Torres"),
    ("Emily", "Jenkins"),
    ("Sarah", "Bennett"),
    ("Michelle", "Patterson"),
    ("Ashley", "Miller"),
    ("Adam", "Ward"),
    ("Alexander", "Torres"),
    ("Nancy", "Sanders"),
    ("Michelle", "Patel"),
    ("Brian", "Bennett"),
    ("Donna", "Hall"),
    ("Emma", "Thompson"),
    ("Robert", "Young"),
    ("William", "Baker"),
    ("Stephen", "Bryant"),
    ("Mark", "Jenkins"),
    ("Jerry", "Thompson"),
    ("Jerry", "Bennett"),
    ("Susan", "Hughes"),
    ("George", "Mitchell"),
    ("Kevin", "Patel"),
    ("Catherine", "Reyes"),
    ("Dorothy", "Baker"),
    ("Alexander", "Clark"),
    ("Henry", "Reyes"),
    ("Jennifer", "Robinson"),
    ("Jack", "Hall"),
    ("Sharon", "Perez"),
    ("John", "Hill"),
    ("Nathan", "Jenkins"),
    ("Janet", "Simmons"),
    ("Jacob", "Simmons"),
    ("Dorothy", "Miller"),
    ("George", "Price"),
    ("Jeffrey", "Robinson"),
    ("Karen", "Evans"),
    ("Christopher", "Smith"),
    ("Eric", "Flores"),
    ("Carl", "Morris"),
    ("Daniel", "Bennett"),
    ("Carl", "Martin"),
    ("Christine", "Cruz"),
    ("Peter", "Jones"),
    ("Christopher", "Jenkins"),
    ("Susan", "Turner"),
    ("Christopher", "Sanders"),
    ("Donald", "Thompson"),
    ("Emily", "Roberts"),
    ("Janet", "Perry"),
    ("Jason", "Perry"),
    ("Michael", "Lee"),
    ("Brandon", "Bryant"),
    ("David", "Smith"),
    ("Robert", "Thompson"),
    ("Gregory", "Powell"),
    ("Ryan", "Gonzales"),
    ("Amanda", "White"),
    ("Melissa", "Parker"),
]


def seed_doublures(apps, schema_editor):
    Doublure = apps.get_model("doublures", "Doublure")
    Doublure.objects.using(schema_editor.connection.alias).bulk_create(
        [Doublure(firstname=firstname, name=name) for firstname, name in DOUBLURES]
    )


def unseed_doublures(apps, schema_editor):
    Doublure = apps.get_model("doublures", "Doublure")
    Doublure.objects.using(schema_editor.connection.alias).all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("doublures", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_doublures, unseed_doublures),
    ]
