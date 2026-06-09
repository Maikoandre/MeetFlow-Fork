import random
from datetime import timedelta
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from events.models import Usuario, Evento, Inscricao, Presenca, Relatorio
from django.utils import timezone


class Command(BaseCommand):
    help = "Populates the database with mock data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Generating mock data...")

        first_names = [
            "Ana","Bruno","Carlos","Daniela","Eduardo","Fernanda","Gabriel",
            "Helena","Igor","Julia","Lucas","Mariana","Nicolas","Olivia",
            "Pedro","Rafaela","Samuel","Tatiana","Vitor","Yasmin"
        ]

        last_names = [
            "Silva","Santos","Oliveira","Souza","Rodrigues","Ferreira","Alves",
            "Pereira","Lima","Gomes","Costa","Ribeiro","Martins","Carvalho",
            "Almeida","Lopes","Soares","Fernandes","Vieira","Barbosa"
        ]

        def get_random_name():
            return f"{random.choice(first_names)} {random.choice(last_names)}"

        # -------------------------
        # ADMIN
        # -------------------------

        user, created = User.objects.get_or_create(
            username="admin",
            defaults={
                "email": "admin@example.com"
            }
        )

        if created:
            user.set_password("password123")
            user.is_superuser = True
            user.is_staff = True
            user.save()

        Usuario.objects.get_or_create(
            user=user,
            defaults={
                "nome": "Administrador",
                "idade": 30,
                "tipo": "admin",
            },
        )

        # -------------------------
        # ORGANIZERS
        # -------------------------

        organizers = []

        for i in range(5):
            username = f"org{i+1}"

            user, created = User.objects.get_or_create(
                username=username,
                defaults={"email": f"{username}@example.com"},
            )

            if created:
                user.set_password("password123")
                user.save()

            Usuario.objects.get_or_create(
                user=user,
                defaults={
                    "nome": get_random_name(),
                    "idade": random.randint(25, 50),
                    "tipo": "organizador",
                },
            )

            organizers.append(user)

        # -------------------------
        # PARTICIPANTS
        # -------------------------

        participants = []

        for i in range(20):
            username = f"user{i+1}"

            user, created = User.objects.get_or_create(
                username=username,
                defaults={"email": f"{username}@example.com"},
            )

            if created:
                user.set_password("password123")
                user.save()

            Usuario.objects.get_or_create(
                user=user,
                defaults={
                    "nome": get_random_name(),
                    "idade": random.randint(18, 40),
                    "tipo": "participante",
                },
            )

            participants.append(user)

        # -------------------------
        # EVENTS
        # -------------------------

        event_titles = [
            "Workshop Python",
            "Palestra IA",
            "Meetup Django",
            "Hackathon Web",
            "Curso React",
            "Seminário DevOps",
            "Conferência Tech",
            "Bootcamp Java",
            "Workshop UX/UI",
            "Encontro Agile",
        ]

        events = []

        for title in event_titles:

            evento, _ = Evento.objects.get_or_create(
                titulo=title,
                defaults={
                    "descricao": f"Descrição detalhada para o evento {title}",
                    "data": timezone.now().date()
                    + timedelta(days=random.randint(-30, 60)),
                    "local": f"Sala {random.randint(100,999)}",
                    "organizador": random.choice(organizers),
                    "aprovado": random.choice([True, True, False]),
                    "publicado": random.choice([True, True, False]),
                },
            )

            events.append(evento)

        # -------------------------
        # INSCRICOES
        # -------------------------

        for _ in range(50):

            participant = random.choice(participants)
            evento = random.choice(events)

            inscricao, created = Inscricao.objects.get_or_create(
                participante=participant,
                evento=evento,
                defaults={
                    "status": random.choice(
                        ["pendente", "confirmado", "cancelado"]
                    )
                },
            )

            if created and inscricao.status == "confirmado":
                if evento.data < timezone.now().date():

                    Presenca.objects.get_or_create(
                        inscricao=inscricao,
                        defaults={"presente": random.choice([True, False])},
                    )

        # -------------------------
        # REPORTS
        # -------------------------

        for evento in events:

            if evento.data < timezone.now().date():

                total_inscritos = evento.inscricoes.count()

                total_presentes = Presenca.objects.filter(
                    inscricao__evento=evento,
                    presente=True,
                ).count()

                Relatorio.objects.get_or_create(
                    evento=evento,
                    defaults={
                        "total_inscritos": total_inscritos,
                        "total_presentes": total_presentes,
                    },
                )

        self.stdout.write(
            self.style.SUCCESS("Successfully populated database")
        )