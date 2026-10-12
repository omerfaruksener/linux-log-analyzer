from main import analiz_yap

def test_analiz_yap_Dogru_SAyiyor_mu():
    #1. Arrange
    sahte_loglar = [
        "INFO Sisteme giris yapildi",
        "ERROR Veritabani baglantisi koptu",
        "WARNING Ram kullanimi %90",
        "ERROR İstek zaman asimina ugradi"
    ]

    #2. Act
    sonuc = analiz_yap(sahte_loglar)

    #3. Assert
    assert sonuc["total_lines"] == 4
    assert sonuc["level_counts"]["INFO"] == 1
    assert sonuc["level_counts"]["ERROR"] == 2
    assert sonuc["level_counts"]["WARNING"] == 1

def test_analiz_yap_filtre_calisiyor_mu():
    # 1. arrange
    sahte_loglar = [
            "INFO Sisteme giris yapildi",
            "ERROR Veritabani baglantisi koptu",
            "WARNING Ram kullanimi %90",
            "ERROR İstek zaman asimina ugradi"
        ]
    #2.act
    sonuc = analiz_yap(sahte_loglar, "ERROR")
    #3.assert
    assert sonuc["level_counts"]["ERROR"] == 2

    assert "INFO" not in sonuc["level_counts"]
    assert "WARNING" not in sonuc["level_counts"]


