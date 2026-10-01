from django.db import migrations

PREMIER_ROLES = [
    ("Ryan", "Roberts"),
    ("Jonathan", "Jones"),
    ("Melissa", "Thomas"),
    ("Jessica", "Cook"),
    ("Catherine", "Rogers"),
    ("James", "Torres"),
    ("Rachel", "Thomas"),
    ("Kevin", "Evans"),
    ("Alexander", "Ross"),
    ("Stephen", "Torres"),
    ("Jessica", "Morris"),
    ("Michelle", "Evans"),
    ("Karen", "Nguyen"),
    ("Brian", "Bailey"),
    ("Michael", "Gray"),
    ("Christopher", "Cooper"),
    ("Sarah", "Lopez"),
    ("Carolyn", "Parker"),
    ("Melissa", "Parker"),
    ("John", "James"),
    ("Sharon", "Richardson"),
    ("Ruth", "Price"),
    ("Eric", "Wright"),
    ("John", "Smith"),
    ("Mark", "Thompson"),
    ("Jason", "Ruiz"),
    ("Margaret", "Richardson"),
    ("Stephen", "Gutierrez"),
    ("Mark", "Cook"),
    ("Jeffrey", "Stewart"),
    ("Benjamin", "James"),
    ("Patrick", "Ward"),
    ("Raymond", "Wright"),
    ("Dennis", "Gonzalez"),
    ("Gary", "Stewart"),
    ("Brandon", "Davis"),
    ("James", "Richardson"),
    ("Mary", "Ruiz"),
    ("Christopher", "Clark"),
    ("David", "Green"),
    ("William", "Patel"),
    ("John", "Morales"),
    ("Jennifer", "Gray"),
    ("George", "Hill"),
    ("Nancy", "Cruz"),
    ("Kevin", "Perez"),
    ("Amy", "Baker"),
    ("Jerry", "Wright"),
    ("Helen", "Murphy"),
    ("Janet", "Morgan"),
    ("Susan", "Morales"),
    ("Donna", "James"),
    ("Timothy", "Gray"),
    ("Stephen", "Sanders"),
    ("Ashley", "Lee"),
    ("Stephen", "Jimenez"),
    ("Andrew", "Hill"),
    ("Mary", "Sanders"),
    ("Jennifer", "Reyes"),
    ("Carol", "Mitchell"),
    ("Stephen", "Carter"),
    ("Brenda", "Turner"),
    ("Jessica", "Mendoza"),
    ("Jessica", "Young"),
    ("William", "Gutierrez"),
    ("Amanda", "Miller"),
    ("Melissa", "Sanders"),
    ("Betty", "Harris"),
    ("Nicole", "Bennett"),
    ("Stephanie", "Morgan"),
    ("Rebecca", "Miller"),
    ("Emma", "Kelly"),
    ("Amy", "Brown"),
    ("Robert", "Chavez"),
    ("Andrew", "Nguyen"),
    ("Amy", "Adams"),
    ("Edward", "Bailey"),
    ("Margaret", "Foster"),
    ("Daniel", "Kelly"),
    ("Jack", "Evans"),
    ("Dorothy", "Baker"),
    ("Nicole", "Miller"),
    ("Sharon", "Evans"),
    ("Patrick", "Gray"),
    ("Samuel", "White"),
    ("Edward", "Robinson"),
    ("Jessica", "Stewart"),
    ("Jacob", "Flores"),
    ("Donald", "Davis"),
    ("Christopher", "Collins"),
    ("Christine", "Campbell"),
    ("Frank", "Rodriguez"),
    ("Dorothy", "Bailey"),
    ("James", "Foster"),
    ("Ruth", "Hall"),
    ("Raymond", "White"),
    ("Larry", "Hall"),
    ("Emily", "Martin"),
    ("Donna", "Martinez"),
    ("Jerry", "Lewis"),
]


def seed_premier_roles(apps, schema_editor):
    PremierRole = apps.get_model("roles", "PremierRole")
    PremierRole.objects.using(schema_editor.connection.alias).bulk_create(
        [
            PremierRole(firstname=firstname, name=name)
            for firstname, name in PREMIER_ROLES
        ]
    )


def unseed_premier_roles(apps, schema_editor):
    PremierRole = apps.get_model("roles", "PremierRole")
    PremierRole.objects.using(schema_editor.connection.alias).all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("roles", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_premier_roles, unseed_premier_roles),
    ]
