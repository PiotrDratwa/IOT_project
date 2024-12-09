# Projekt IoT: Monitorowanie Temperatura i Mowa w Czasie Rzeczywistym

Projekt IoT składa się z kilku zintegrowanych modułów, które współdziałają, aby mierzyć, przetwarzać i wyświetlać dane w czasie rzeczywistym. Wykorzystuje technologie takie jak **ESP8266**, **MQTT**, **Docker**, **Python** oraz **Whisper AI**. Poniżej przedstawiamy szczegółowy opis głównych funkcji i technologii użytych w projekcie.

----------

## Główne Funkcje Projektu

### 1. **Pomiar temperatury** 🌡️

Czujnik **DS18B20** podłączony do mikrokontrolera **ESP8266** zbiera dane dotyczące temperatury.

-   **Wyświetlanie danych**: Wynik jest wyświetlany w terminalu Arduino oraz przesyłany do brokera MQTT.

----------

### 2. **Speech-to-Text** 🗣️

Moduł rozpoznawania mowy oparty na **Pythonie** i modelu **Whisper AI** konwertuje dźwięk na tekst.

-   **Przesyłanie danych**: Przesłany tekst wyświetlany jest w terminalu i wysyłany do brokera MQTT.
-   **Odczyt przez ESP8266**: ESP8266 odbiera dane z brokera, a wynik jest wyświetlany zarówno w terminalu Arduino, jak i na wyświetlaczu LCD podłączonym do płytki.

----------

### 3. **Przetwarzanie Danych** ⚙️

Skrypt w **Pythonie** subskrybuje dane z brokera MQTT, zapisuje je w bazie **InfluxDB**.

-   **Wizualizacja zmian**: Zmiany temperatury są wizualizowane na wykresach przy użyciu narzędzia **Grafana**.

----------

## 🛠️ Technologie

### 1. **ESP8266** z czujnikiem **DS18B20** oraz wyświetlaczem LCD

-   Mikrokontroler zbiera dane z czujnika temperatury i wyświetla wyniki na ekranie LCD.

### 2. **Broker MQTT**

-   Broker MQTT odpowiada za przesyłanie danych pomiędzy urządzeniami.
-   Implementacja mechanizmów autoryzacji (nazwa użytkownika, hasło, TLS) zapewnia bezpieczeństwo komunikacji.

### 3. **Docker**

-   **InfluxDB** i **Grafana** działają w kontenerach Dockerowych, co zapewnia łatwą konfigurację i izolację środowisk.

### 4. **Python**

-   **paho-mqtt**: Biblioteka do obsługi MQTT w Pythonie.
-   **influxdb-client**: Używana do zapisu danych do bazy danych InfluxDB.
-   **Whisper**: Model AI do rozpoznawania mowy i konwersji audio na tekst.

----------

## ⚙️ Wymagania Systemowe

-   **Docker Engine** oraz **Docker Compose**: Niezbędne do uruchomienia kontenerów z InfluxDB i Grafaną.
-   **Python 3.8** lub nowszy: Potrzebny do uruchomienia skryptów w Pythonie i komunikacji z brokerem MQTT.
-   **Arduino IDE**: Do zarządzania mikrokontrolerem ESP8266.

----------

## 🔧 Schemat Działania

1.  **Mikrokontroler ESP8266** zbiera dane z czujnika DS18B20.
2.  **MQTT Broker** przesyła dane o temperaturze do aplikacji.
3.  **Model Whisper AI** przetwarza mowę na tekst i wysyła wynik do brokera MQTT.
4.  **Python** zapisuje dane w bazie **InfluxDB**.
5.  **Grafana** wizualizuje dane na wykresach, prezentując zmiany temperatury w czasie rzeczywistym.

----------

### Podsumowanie

Projekt umożliwia efektywne zbieranie i przetwarzanie danych, wykorzystując nowoczesne technologie IoT oraz sztuczną inteligencję. Dzięki zastosowaniu **MQTT**, **Docker**, **Python** i **Whisper**, całość systemu jest skalowalna, elastyczna i bezpieczna.

### Autorzy
Piotr Dratwa i Jakub Kaczmarzewski
