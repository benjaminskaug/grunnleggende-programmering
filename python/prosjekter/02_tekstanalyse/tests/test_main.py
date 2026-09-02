from tekstanalyse.main import finn_antall_tegn, finn_unike_ord, lag_ordliste, finn_lengste_ord, lag_frekvens, finn_mest_brukte_ord



def test_finn_antall_tegn_med_tekst():
    assert finn_antall_tegn("Skogen er vakker!") == 17


def test_finn_antall_tegn_teller_mellomrom_og_tegnsetting():
    assert finn_antall_tegn("Hei!   ") == 7


def test_finn_antall_tegn_uten_tekst():
    assert finn_antall_tegn("") == 0


def test_finn_unike_ord_med_ulike_ord():
    assert finn_unike_ord(["skog", "fjell", "elv", "hav", "skog"]) == 4


def test_finn_unike_ord_med_like_ord():
    assert finn_unike_ord(["skog", "skog", "skog"]) == 1


def test_finn_unike_ord_uten_tekst():
    assert finn_unike_ord([]) == 0


def test_lag_ordliste():
    assert lag_ordliste("Skogen er vakker!") == ["skogen", "er", "vakker"]


def test_lag_ordliste_med_like_ord():
    assert lag_ordliste("Skog skog SKOG") == ["skog", "skog", "skog"]


def test_lag_ordliste_med_mellomrom_rundt_tekst():
    assert lag_ordliste("   Skogen er vakker!   ") == ["skogen", "er", "vakker"]


def test_finn_lengste_ord():
    assert finn_lengste_ord(["skog", "blomster", "fjell"]) == "blomster"


def test_finn_lengste_ord_med_like_lange_ord():
    assert finn_lengste_ord(["blader", "sommer", "vinter"]) == "blader"


def test_lag_frekvens():
    assert lag_frekvens(["skog", "er", "skog"]) == {"skog": 2, "er": 1}


def test_lag_frekvens_uten_ord():
    assert lag_frekvens([]) == {}


def test_finn_mest_brukte_ord():
    assert finn_mest_brukte_ord({"skog": 3, "fjell": 1, "elv": 2}) == "skog"


def test_finn_mest_brukte_ord_uten_ord():
    assert finn_mest_brukte_ord({}) == "Ingen ord"


def test_finn_mest_brukte_ord_fra_tekst_via_ordliste_og_frekvens():
    ordliste = lag_ordliste(
        "Skogen er både vakker og rolig, og full av liv."
    )
    frekvens = lag_frekvens(ordliste)

    assert finn_mest_brukte_ord(frekvens) == "og"


def test_finn_mest_brukte_ord_med_ett_ord():
    assert finn_mest_brukte_ord({"sannsynligvis": 1}) == "sannsynligvis"


def test_finn_lengste_ord_fra_tekst_via_ordliste():
    ordliste = lag_ordliste(
        "Skogen er både vakker og rolig, og full av dyreliv."
    )

    assert finn_lengste_ord(ordliste) == "dyreliv"


def test_finn_lengste_ord_fra_tekst_via_ordliste_med_bare_tegnsetting():
    ordliste = lag_ordliste("!!!")

    assert finn_lengste_ord(ordliste) == "Ingen ord"
