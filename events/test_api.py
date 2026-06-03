from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Usuario, Evento, Inscricao, Presenca, Relatorio
from datetime import date

class MeetFlowAPITests(APITestCase):
    def setUp(self):
        # Create standard test users
        self.user = User.objects.create_user(username='testapiuser', password='password123')
        self.organizer = User.objects.create_user(username='organizerapi', password='password123')
        self.participant = User.objects.create_user(username='participantapi', password='password123')

        # Create profiles
        self.profile = Usuario.objects.create(
            user=self.user,
            nome="Test User",
            idade=30,
            tipo="admin"
        )
        self.organizer_profile = Usuario.objects.create(
            user=self.organizer,
            nome="Organizer User",
            idade=35,
            tipo="organizador"
        )
        self.participant_profile = Usuario.objects.create(
            user=self.participant,
            nome="Participant User",
            idade=25,
            tipo="participante"
        )

        # Create base objects for details tests
        self.evento = Evento.objects.create(
            titulo="Python Conference",
            descricao="Annual Python conference",
            data=date.today(),
            local="Convention Center",
            organizador=self.organizer,
            aprovado=True,
            publicado=True
        )

        self.inscricao = Inscricao.objects.create(
            evento=self.evento,
            participante=self.participant,
            status="pendente"
        )

        self.presenca = Presenca.objects.create(
            inscricao=self.inscricao,
            presente=False
        )

        self.relatorio = Relatorio.objects.create(
            evento=self.evento,
            total_inscritos=1,
            total_presentes=0
        )

    # --- Usuario API Tests ---
    def test_usuario_list_get(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_usuario_post(self):
        self.client.force_authenticate(user=self.user)
        new_user = User.objects.create_user(username='newapiuser', password='password123')
        data = {
            "user": new_user.id,
            "nome": "New User Profile",
            "idade": 28,
            "tipo": "participante"
        }
        response = self.client.post('/api/users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Usuario.objects.filter(nome="New User Profile").count(), 1)

    def test_usuario_retrieve_get(self):
        response = self.client.get(f'/api/users/{self.profile.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], "Test User")

    def test_usuario_put(self):
        self.client.force_authenticate(user=self.user)
        data = {
            "user": self.user.id,
            "nome": "Updated Test User Name",
            "idade": 31,
            "tipo": "admin"
        }
        response = self.client.put(f'/api/users/{self.profile.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.nome, "Updated Test User Name")

    def test_usuario_patch(self):
        self.client.force_authenticate(user=self.user)
        data = {
            "nome": "Patched Test User Name"
        }
        response = self.client.patch(f'/api/users/{self.profile.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.nome, "Patched Test User Name")

    def test_usuario_delete(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f'/api/users/{self.profile.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Usuario.objects.filter(id=self.profile.id).count(), 0)

    # --- Evento API Tests ---
    def test_evento_list_get(self):
        response = self.client.get('/api/eventos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_evento_post(self):
        self.client.force_authenticate(user=self.organizer)
        data = {
            "titulo": "Django Workshop",
            "descricao": "Practical workshop about Django",
            "data": "2026-08-10",
            "local": "Online",
            "organizador": self.organizer.id,
            "aprovado": False,
            "publicado": False
        }
        response = self.client.post('/api/eventos/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Evento.objects.filter(titulo="Django Workshop").count(), 1)

    def test_evento_retrieve_get(self):
        response = self.client.get(f'/api/eventos/{self.evento.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['titulo'], "Python Conference")

    def test_evento_put(self):
        self.client.force_authenticate(user=self.organizer)
        data = {
            "titulo": "Python Conference 2026",
            "descricao": "Annual Python conference updated",
            "data": str(date.today()),
            "local": "Convention Center Room B",
            "organizador": self.organizer.id,
            "aprovado": True,
            "publicado": True
        }
        response = self.client.put(f'/api/eventos/{self.evento.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.evento.refresh_from_db()
        self.assertEqual(self.evento.titulo, "Python Conference 2026")

    def test_evento_patch(self):
        self.client.force_authenticate(user=self.organizer)
        data = {
            "local": "Online Webinar"
        }
        response = self.client.patch(f'/api/eventos/{self.evento.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.evento.refresh_from_db()
        self.assertEqual(self.evento.local, "Online Webinar")

    def test_evento_delete(self):
        self.client.force_authenticate(user=self.organizer)
        response = self.client.delete(f'/api/eventos/{self.evento.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Evento.objects.filter(id=self.evento.id).count(), 0)

    # --- Inscricao API Tests ---
    def test_inscricao_list_get(self):
        response = self.client.get('/api/inscricoes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_inscricao_post(self):
        self.client.force_authenticate(user=self.participant)
        new_event = Evento.objects.create(
            titulo="Go Meetup",
            descricao="Meetup for Go developers",
            data=date.today(),
            local="Online",
            organizador=self.organizer
        )
        data = {
            "evento": new_event.id,
            "participante": self.participant.id,
            "status": "pendente"
        }
        response = self.client.post('/api/inscricoes/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Inscricao.objects.filter(evento=new_event).count(), 1)

    def test_inscricao_retrieve_get(self):
        response = self.client.get(f'/api/inscricoes/{self.inscricao.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_inscricao_put(self):
        self.client.force_authenticate(user=self.organizer)
        data = {
            "evento": self.evento.id,
            "participante": self.participant.id,
            "status": "confirmado"
        }
        response = self.client.put(f'/api/inscricoes/{self.inscricao.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.inscricao.refresh_from_db()
        self.assertEqual(self.inscricao.status, "confirmado")

    def test_inscricao_patch(self):
        self.client.force_authenticate(user=self.organizer)
        data = {
            "status": "cancelado"
        }
        response = self.client.patch(f'/api/inscricoes/{self.inscricao.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.inscricao.refresh_from_db()
        self.assertEqual(self.inscricao.status, "cancelado")

    def test_inscricao_delete(self):
        self.client.force_authenticate(user=self.organizer)
        response = self.client.delete(f'/api/inscricoes/{self.inscricao.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Inscricao.objects.filter(id=self.inscricao.id).count(), 0)

    # --- Presenca API Tests ---
    def test_presenca_list_get(self):
        response = self.client.get('/api/presencas/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_presenca_post(self):
        self.client.force_authenticate(user=self.organizer)
        new_insc = Inscricao.objects.create(
            evento=self.evento,
            participante=self.user,
            status="confirmado"
        )
        data = {
            "inscricao": new_insc.id,
            "presente": True
        }
        response = self.client.post('/api/presencas/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Presenca.objects.filter(inscricao=new_insc).count(), 1)

    def test_presenca_retrieve_get(self):
        response = self.client.get(f'/api/presencas/{self.presenca.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_presenca_put(self):
        self.client.force_authenticate(user=self.organizer)
        data = {
            "inscricao": self.inscricao.id,
            "presente": True
        }
        response = self.client.put(f'/api/presencas/{self.presenca.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.presenca.refresh_from_db()
        self.assertTrue(self.presenca.presente)

    def test_presenca_patch(self):
        self.client.force_authenticate(user=self.organizer)
        data = {
            "presente": True
        }
        response = self.client.patch(f'/api/presencas/{self.presenca.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.presenca.refresh_from_db()
        self.assertTrue(self.presenca.presente)

    def test_presenca_delete(self):
        self.client.force_authenticate(user=self.organizer)
        response = self.client.delete(f'/api/presencas/{self.presenca.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Presenca.objects.filter(id=self.presenca.id).count(), 0)

    # --- Relatorio API Tests ---
    def test_relatorio_list_get(self):
        response = self.client.get('/api/relatorios/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_relatorio_post(self):
        self.client.force_authenticate(user=self.organizer)
        data = {
            "evento": self.evento.id,
            "total_inscritos": 10,
            "total_presentes": 8
        }
        response = self.client.post('/api/relatorios/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Relatorio.objects.filter(total_inscritos=10).count(), 1)

    def test_relatorio_retrieve_get(self):
        response = self.client.get(f'/api/relatorios/{self.relatorio.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_relatorio_put(self):
        self.client.force_authenticate(user=self.organizer)
        data = {
            "evento": self.evento.id,
            "total_inscritos": 15,
            "total_presentes": 12
        }
        response = self.client.put(f'/api/relatorios/{self.relatorio.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.relatorio.refresh_from_db()
        self.assertEqual(self.relatorio.total_inscritos, 15)

    def test_relatorio_patch(self):
        self.client.force_authenticate(user=self.organizer)
        data = {
            "total_presentes": 5
        }
        response = self.client.patch(f'/api/relatorios/{self.relatorio.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.relatorio.refresh_from_db()
        self.assertEqual(self.relatorio.total_presentes, 5)

    def test_relatorio_delete(self):
        self.client.force_authenticate(user=self.organizer)
        response = self.client.delete(f'/api/relatorios/{self.relatorio.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Relatorio.objects.filter(id=self.relatorio.id).count(), 0)
