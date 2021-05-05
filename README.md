# Label Scripts
Collection of scripts used to automate business tasks.

### Dependencies

- Python3
- Pandas
- Pytest (optional)

## Release Dates

Generates a timeline of deadlines for record project from CSV.

#### Usage

Standard usage outputs to clipboard and can be pasted.  

Optional flag -e outputs in emacs org-mode format, qualifying each deadline as a TODO item.  

`release.py [-e] [orgmode file]`

## ISRC Generator

Python script to generate ISRCs from the command line.

#### Info
ISRC codes are 12 characters long, and follow the following conventions.

*Format: CC-XXX-YY-NNNNN*

- "CC" is the two character country code for the ISRC issuer
- "XXX" is the three character registrant code of the ISRC issuer
- "YY" are the last two digits of the reference year
- "NNNNN" is a 5-digit code that identifies the recording

#### Features
- Default values for country code and registrant code are saved in locally in a JSON
- Default year is based on local date
- Identifying 5 digit code is composed of 3 digit catalog identifier and 2 digit track number
- Output generated in standard out as well as CSV


#### Usage

`python isrc.py`

## Fill PDF

Fills IPR and CueSheets templates from AtoZ, using release info from json.

#### Info
Requires a JSON (info.json) of the following format:

`{ "catalog_number": "",
	"artist": "",
	"album_name": "",
	"speed": "",
	"genre": "",
	"a":[
      "track_number": "",
			"track_name": "",
			"length": ""
      ]
      ,
  "b":[
      "track_number": "",
      "track_name": "",
      "length": ""
      ]
}`




