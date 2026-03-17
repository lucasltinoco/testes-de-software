import unittest
import datetime


class TestMain(unittest.TestCase):
    def setUp(self):
        pass

    def test_cria_data_natal_2025(self):
        # Fixture Setup
        # Exercise SUT
        natal_2025 = datetime.date(2025, 12, 25)
        # Result Verification
        self.assertEqual(2025, natal_2025.year)
        self.assertEqual(12, natal_2025.month)
        assert natal_2025.day == 25
        # Fixture Teardown

    def test_cria_data_dia_negativo_invalido(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            data_invalida = datetime.date(2024, 3, -1)
        # Result Verification
        # Fixture Teardown

    def test_cria_data_mes_negativo_invalido(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            data_invalida = datetime.date(2024, -1, 3)
        # Result Verification
        # Fixture Teardown

    def test_cria_data_ano_negativo_invalido(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            data_invalida = datetime.date(-1, 3, 10)
        # Result Verification
        # Fixture Teardown

    def test_cria_data_de_ano_bissexto_invalido(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            dia_29_fevereiro = datetime.date(2023, 2, 29)
        # Result Verification
        # Fixture Teardown

    def test_cria_data_mes_superior_ao_maximo_invalido(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            mes_13 = datetime.date(2024, 13, 4)
        # Result Verification
        # Fixture Teardown

    def test_cria_data_sem_dia(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(TypeError):
            sem_dia = datetime.date(2024, 13)
        # Result Verification
        # Fixture Teardown

    def test_cria_data_sem_mes(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(TypeError):
            sem_mes = datetime.date(year=2024, day=4)
        # Result Verification
        # Fixture Teardown

    def test_cria_data_sem_ano(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(TypeError):
            sem_ano = datetime.date(month=12, day=4)
        # Result Verification
        # Fixture Teardown

    def test_cria_data_sem_argumento(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(TypeError):
            sem_argumento = datetime.date()
        # Result Verification
        # Fixture Teardown

    def test_cria_data_com_argumento_string_invalido(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(TypeError):
            data_invalida = datetime.date("2024", "12", "4")
        # Result Verification
        # Fixture Teardown

    def test_cria_data_com_argumento_float_invalido(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(TypeError):
            data_invalida = datetime.date(2024.0, 12.0, 4.0)
        # Result Verification
        # Fixture Teardown

    def test_replace_de_mes(self):
        # Fixture Setup
        ano = datetime.date(2024, 1, 15)
        # Exercise SUT
        ano_fevereiro = ano.replace(month=2)
        # Result Verification
        self.assertEqual(ano_fevereiro.year, 2024)
        self.assertEqual(ano_fevereiro.month, 2)
        self.assertEqual(ano_fevereiro.day, 15)
        # Fixture Teardown

    def test_replace_de_dia(self):
        # Fixture Setup
        ano = datetime.date(2024, 1, 15)
        # Exercise SUT
        ano_fevereiro = ano.replace(day=28)
        # Result Verification
        self.assertEqual(ano_fevereiro.year, 2024)
        self.assertEqual(ano_fevereiro.month, 1)
        self.assertEqual(ano_fevereiro.day, 28)
        # Fixture Teardown

    def test_replace_de_ano(self):
        # Fixture Setup
        ano = datetime.date(2024, 1, 15)
        # Exercise SUT
        ano_fevereiro = ano.replace(year=2029)
        # Result Verification
        self.assertEqual(ano_fevereiro.year, 2029)
        self.assertEqual(ano_fevereiro.month, 1)
        self.assertEqual(ano_fevereiro.day, 15)
        # Fixture Teardown

    def test_replace_com_argumento_invalido(self):
        # Fixture Setup
        ano = datetime.date(2024, 1, 15)
        # Exercise SUT
        with self.assertRaises(ValueError):
            ano.replace(month=13)
        with self.assertRaises(ValueError):
            ano.replace(day=32)
        with self.assertRaises(ValueError):
            ano.replace(year=-1)
        # Result Verification
        self.assertEqual(ano.year, 2024)
        self.assertEqual(ano.month, 1)
        self.assertEqual(ano.day, 15)
        # Fixture Teardown

    def test_transformacao_ordinal_do_primeiro_dia_dC(self):
        # Fixture Setup
        ano = datetime.date(1, 1, 1)
        # Exercise SUT
        ordinal = ano.toordinal()
        # Result Verification
        self.assertEqual(ordinal, 1)
        # Fixture Teardown

    def test_weekday_conhecido_segunda(self):
        # Fixture Setup
        data = datetime.date(2026, 3, 16)
        # Exercise SUT
        dia_semana = data.weekday()
        # Result Verification
        self.assertEqual(dia_semana, 0)
        # Fixture Teardown

    def test_weekday_conhecido_terca(self):
        # Fixture Setup
        data = datetime.date(2026, 3, 17)
        # Exercise SUT
        dia_semana = data.weekday()
        # Result Verification
        self.assertEqual(dia_semana, 1)
        # Fixture Teardown

    def test_weekday_conhecido_quarta(self):
        # Fixture Setup
        data = datetime.date(2026, 3, 18)
        # Exercise SUT
        dia_semana = data.weekday()
        # Result Verification
        self.assertEqual(dia_semana, 2)
        # Fixture Teardown

    def test_weekday_conhecido_quinta(self):
        # Fixture Setup
        data = datetime.date(2026, 3, 19)
        # Exercise SUT
        dia_semana = data.weekday()
        # Result Verification
        self.assertEqual(dia_semana, 3)
        # Fixture Teardown

    def test_weekday_conhecido_sexta(self):
        # Fixture Setup
        data = datetime.date(2026, 3, 20)
        # Exercise SUT
        dia_semana = data.weekday()
        # Result Verification
        self.assertEqual(dia_semana, 4)
        # Fixture Teardown

    def test_cria_horario_corretamente(self):
        # Fixture Setup
        # Exercise SUT
        hora = datetime.time(hour=11, minute=56, second=2)
        # Result Verification
        self.assertEqual(hora.hour, 11)
        self.assertEqual(hora.minute, 56)
        self.assertEqual(hora.second, 2)
        # Fixture Teardown

    def test_output_correto_de_horario(self):
        # Fixture Setup
        # Exercise SUT
        hora = datetime.time(hour=11, minute=56, second=2)
        # Result Verification
        self.assertEqual(hora.strftime("%I:%M:%S"), "11:56:02")
        # Fixture Teardown

    def test_criar_datetime_completo(self):
        # Fixture Setup
        # Exercise SUT
        data_tempo = datetime.datetime(2024, 12, 25, 15, 30, 45)
        # Result Verification
        self.assertEqual(data_tempo.year, 2024)
        self.assertEqual(data_tempo.month, 12)
        self.assertEqual(data_tempo.day, 25)
        self.assertEqual(data_tempo.hour, 15)
        self.assertEqual(data_tempo.minute, 30)
        self.assertEqual(data_tempo.second, 45)
        # Fixture Teardown

    def test_criar_datetime_sem_hora(self):
        # Fixture Setup
        # Exercise SUT
        data_tempo = datetime.datetime(2024, 12, 25)
        # Result Verification
        self.assertEqual(data_tempo.hour, 0)
        self.assertEqual(data_tempo.minute, 0)
        self.assertEqual(data_tempo.second, 0)
        # Fixture Teardown

    def test_datetime_strftime_formatacao(self):
        # Fixture Setup
        data_tempo = datetime.datetime(2024, 12, 25, 15, 30, 45)
        # Exercise SUT
        formatado = data_tempo.strftime("%Y-%m-%d %H:%M:%S")
        # Result Verification
        self.assertEqual(formatado, "2024-12-25 15:30:45")
        # Fixture Teardown

    def test_soma_de_semanas_dias_horas_minutos_e_segundos_de_um_ano_bate_com_365_dias(
        self,
    ):
        # Fixture Setup
        ano = datetime.timedelta(days=365)
        # Exercise SUT
        outro_ano = datetime.timedelta(
            weeks=40, days=84, hours=23, minutes=50, seconds=600
        )
        # Result Verification
        self.assertEqual(ano, outro_ano)
        # Fixture Teardown

    def test_multiplica_datas_corretamente(self):
        # Fixture Setup
        ano = datetime.timedelta(days=365)
        # Exercise SUT
        dez_anos = 10 * ano
        # Result Verification
        self.assertEqual(dez_anos.days, 3650)
        # Fixture Teardown

    def test_subtrai_datas_corretamente(self):
        # Fixture Setup
        ano = datetime.timedelta(days=365)
        dez_anos = datetime.timedelta(days=3650)
        # Exercise SUT
        nove_anos = dez_anos - ano
        # Result Verification
        self.assertEqual(nove_anos.days, 3650 - 365)
        # Fixture Teardown

    def test_divide_timedelta_corretamente(self):
        # Fixture Setup
        dez_anos = datetime.timedelta(days=3650)
        # Exercise SUT
        cinco_anos = dez_anos / 2
        # Result Verification
        self.assertEqual(cinco_anos.days, 1825)
        # Fixture Teardown

    def test_timedelta_negativo_valido(self):
        # Fixture Setup
        # Exercise SUT
        tempo_negativo = datetime.timedelta(days=-10)
        # Result Verification
        self.assertEqual(tempo_negativo.days, -10)
        # Fixture Teardown

    def test_timedelta_zero(self):
        # Fixture Setup
        # Exercise SUT
        tempo_zero = datetime.timedelta()
        # Result Verification
        self.assertEqual(tempo_zero.days, 0)
        self.assertEqual(tempo_zero.seconds, 0)
        # Fixture Teardown

    def test_timedelta_modulo_corretamente(self):
        # Fixture Setup
        dez_anos = datetime.timedelta(days=3650)
        # Exercise SUT
        resto = dez_anos % datetime.timedelta(days=365)
        # Result Verification
        self.assertEqual(resto.days, 0)
        # Fixture Teardown
