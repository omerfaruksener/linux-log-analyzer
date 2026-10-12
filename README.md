Python ve argparse kullanilarak gelistirilmis, Linux log dosyalarini analiz eden, log seviyelerine (INFO, ERROR, WARNING) gore filtreleme yapan ve JSON formatinda rapor ureten CLI araci.

- Python 3
- argparse (Terminal parametreleri icin)
- json (Rapor ciktisi uretmek icin)
- pytest (Otomatik birim testleri icin)
- collections.Counter (Verileri gruplamak ve saymak icin)

1. Repoyu klonlayin.
2. Sanal ortami kurun: python -m venv venv
3. Aktif edin: source venv/bin/activate
4. Paketleri yukleyin: pip install -r requirements.txt
5. Calistirin: python main.py sample.log --level ERROR
6. Testleri calistirin: pytest