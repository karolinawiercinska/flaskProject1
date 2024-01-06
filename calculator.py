from datetime import datetime, timedelta
import math


class Calculator():
    """ Klasa przeliczająca diety na podstawie formy i danych o krajach.


    Dostępne pola:

    is_country - true jeżeli są dane o podróży krajowej

    country_travel_time_days, country_travel_time_hours, country_travel_time_minutes - czas podróży

    country_diet - wartość diety

    country_currency - waluta


    is_international - true jeżeli są dane o podróży zagranicznej

    international_travel_time_days, international_travel_time_hours, international_travel_time_minutes - czas podróży

    international_diet - wartość diety

    international_currency - waluta
    """

    def __init__(self, form, countries_data):
        poland_full_day = 45
        poland_half_day = poland_full_day / 2
        poland_quarter_day = poland_full_day / 4
        poland_accommodation = 67.5
        poland_public_transport = 9

        self.is_country = form['kraj_start'] != ''
        self.is_international = form['zagra_start'] != ''

        if self.is_country:
            self.country_diet = 0
            self.country_currency = 'PLN'

            start_datetime = datetime.strptime(form['kraj_start'], '%Y-%m-%dT%H:%M')
            end_datetime = datetime.strptime(form['kraj_koniec'], '%Y-%m-%dT%H:%M')
            country_travel_time = end_datetime - start_datetime

            if country_travel_time < timedelta(0):
                country_travel_time = timedelta(0)

            # Czas podróży
            self.country_travel_time_days = country_travel_time.days
            travelled_hours = country_travel_time.seconds / 3600
            self.country_travel_time_hours = math.trunc(travelled_hours)
            self.country_travel_time_minutes = math.trunc(
                round((travelled_hours - math.trunc(travelled_hours)) * 60, 0))

            # Obliczanie bazowej diety
            if self.country_travel_time_days == 0 and (8 <= travelled_hours and travelled_hours <= 12):
                self.country_diet = poland_half_day
            elif self.country_travel_time_days == 0 and travelled_hours > 12:
                self.country_diet = poland_full_day
            elif self.country_travel_time_days > 0:
                self.country_diet = poland_full_day * self.country_travel_time_days
                if travelled_hours >= 8:
                    self.country_diet += poland_full_day
                else:
                    self.country_diet += poland_half_day

            # Odliczanie posiłków
            self.country_diet -= int(form['kraj_sniadanie']) * poland_quarter_day
            self.country_diet -= int(form['kraj_obiad']) * poland_half_day
            self.country_diet -= int(form['kraj_kolacja']) * poland_quarter_day

            # Noclegi i komunikacja
            self.country_diet += int(form['kraj_noclegi']) * poland_accommodation
            self.country_diet += int(form['kraj_komunikacja']) * poland_public_transport

            # Ustawiamy dietę na 0 jeżeli jest ujemna lub w praktyce nie podróżowaliśmy
            if self.country_diet < 0 or country_travel_time == timedelta(0):
                self.country_diet = 0

        if self.is_international:
            country_data = countries_data.loc[countries_data['Kraj'] == form['country']]

            self.international_diet = 0
            self.international_currency = country_data['Waluta'].values[0]

            base_payment = country_data['Dieta'].values[0]
            half_payment = base_payment / 2
            third_payment = base_payment / 3
            quarter_payment = base_payment / 4
            accommodation = country_data['Nocleg'].values[0]

            start_datetime = datetime.strptime(form['zagra_start'], '%Y-%m-%dT%H:%M')
            end_datetime = datetime.strptime(form['zagra_koniec'], '%Y-%m-%dT%H:%M')
            international_travel_time = end_datetime - start_datetime

            if international_travel_time < timedelta(0):
                international_travel_time = timedelta(0)

            # Czas podróży
            self.international_travel_time_days = international_travel_time.days
            travelled_hours = international_travel_time.seconds / 3600
            self.international_travel_time_hours = math.trunc(travelled_hours)
            self.international_travel_time_minutes = math.trunc(
                round((travelled_hours - math.trunc(travelled_hours)) * 60, 0))

            # Obliczanie bazowej diety
            self.international_diet = base_payment * self.international_travel_time_days

            if travelled_hours < 8:
                self.international_diet += third_payment
            elif 8 <= travelled_hours and travelled_hours <= 12:
                self.international_diet += half_payment
            else:
                self.international_diet += base_payment

            # Odliczanie posiłków
            self.international_diet -= int(form['zagra_sniadanie']) * quarter_payment
            self.international_diet -= int(form['zagra_obiad']) * half_payment
            self.international_diet -= int(form['zagra_kolacja']) * quarter_payment

            # Noclegi
            self.international_diet += int(form['zagra_noclegi']) * accommodation

            # Ustawiamy dietę na 0 jeżeli jest ujemna lub w praktyce nie podróżowaliśmy
            if self.international_diet < 0 or international_travel_time == timedelta(0):
                self.international_diet = 0

            # Przy niektórych państwach może nie wyjść ładnie
            self.international_diet = round(self.international_diet, 2)

    def get_country_travel_time(self):
        """ Pobiera czas podróży w kraju w postaci stringa"""

        if not self.is_country:
            return "Brak"

        return f'{self.country_travel_time_days} dni {self.country_travel_time_hours} godzin {self.country_travel_time_minutes} minut'

    def get_international_travel_time(self):
        """ Pobiera czas podróży za granicą w postaci stringa"""

        if not self.is_international:
            return "Brak"

        return f'{self.international_travel_time_days} dni {self.international_travel_time_hours} godzin {self.international_travel_time_minutes} minut'

    def get_total_travel_time(self):
        """ Pobiera łączny czas podróży w postaci stringa"""

        total_time = timedelta(0)

        if self.is_country:
            total_time += timedelta(days=self.country_travel_time_days, hours=self.country_travel_time_hours,
                                    minutes=self.country_travel_time_minutes)

        if self.is_international:
            total_time += timedelta(days=self.international_travel_time_days,
                                    hours=self.international_travel_time_hours,
                                    minutes=self.international_travel_time_minutes)

        total_days = total_time.days
        travelled_hours = total_time.seconds / 3600
        total_hours = math.trunc(travelled_hours)
        total_minutes = math.trunc(round((travelled_hours - math.trunc(travelled_hours)) * 60, 0))

        return f'{total_days} dni {total_hours} godzin {total_minutes} minut'

    def get_country_diet(self):
        """ Pobiera krajową dietę jako string"""

        if not self.is_country:
            return "0.00 PLN"

        return f'{self.country_diet:.2f} {self.country_currency}'

    def get_international_diet(self):
        """ Pobiera zagraniczną dietę jako string"""

        if not self.is_international:
            return "0.00 PLN"

        return f'{self.international_diet:.2f} {self.international_currency}'

    def get_diet(self):
        """ Zwraca całkowitą dietę zależną od obecności części podróży"""

        diet = ""

        if self.is_country:
            diet += self.get_country_diet()
            diet += " "

        if self.is_international:
            # Dodaj "oraz" tylko jeśli jest zarówno podróż krajowa, jak i zagraniczna
            if self.is_country and self.is_international:
                diet += "oraz "
            diet += self.get_international_diet()

        if not self.is_country and not self.is_international:
            diet = "0.00 PLN"

        return diet.strip()