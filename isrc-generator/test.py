import pytest
import json
import os

from isrc import make_settings_file, Isrcs, retrieve_settings

def test_can_make_setting_file():
    filename = make_settings_file()
    assert filename == 'settings.json'
    with open(filename, 'r') as f:
        assert json.loads(f.read()) == {
                'country_code': '',
                'isrc_registrant': '',
                }

def test_can_make_isrcs():
    test_isrcs = Isrcs('QZ', '123', '20', '012', 10)
    assert test_isrcs.country_code == 'QZ'
    isrcs = test_isrcs.make_isrcs()
    assert len(isrcs) == 10
    for i in range(10):
        assert isrcs[i] == f'QZ12320012{i+1:02d}'
        

def test_can_retrieve_settings():
    settings_json = retrieve_settings()
    assert len(settings_json) > 0
    assert settings_json['country_code'] == ''
    assert settings_json['isrc_registrant'] == ''

def test_can_save_settings():
    settings_json = retrieve_settings()
    test_isrcs = Isrcs('QZ', '123', '20', '012', 10)
    test_isrcs.save_settings()
    setting_json = retrieve_settings()
    assert setting_json['country_code'] == 'QZ'
    assert setting_json['isrc_registrant'] == '123'
    assert setting_json['year'] == '20'
    
def test_can_make_csv():
    test_isrcs = Isrcs('QZ', '123', '20', '012', 10)
    df = test_isrcs.make_csv()
    assert len(df) > 0 
    assert df['track_number'][0] == 1
    assert os.path.exists('isrcs.csv') 
    os.remove('isrcs.csv')
