from django.db import migrations
from django.utils import timezone


def create_mythical_creatures_poll(apps, schema_editor):
    Question = apps.get_model("polls", "Question")
    Choice = apps.get_model("polls", "Choice")

    question = Question.objects.using(schema_editor.connection.alias).create(
        question_text="Which mythical creature would you most want as a pet?",
        pub_date=timezone.now(),
    )

    for creature in ["Dragon", "Phoenix", "Griffin", "Unicorn"]:
        Choice.objects.using(schema_editor.connection.alias).create(
            question=question,
            choice_text=creature,
            votes=0,
        )


def remove_mythical_creatures_poll(apps, schema_editor):
    Question = apps.get_model("polls", "Question")
    Question.objects.using(schema_editor.connection.alias).filter(
        question_text="Which mythical creature would you most want as a pet?"
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(
            create_mythical_creatures_poll,
            remove_mythical_creatures_poll,
        ),
    ]
