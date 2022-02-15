{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "unique-million",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "id": "surprised-danger",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv('freight_2021B.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "id": "explicit-jaguar",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = df[['description', 'net']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "id": "hispanic-default",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['catalog_number'] = (\n",
    "                df['description'].str.slice(0,2)\n",
    "                + '-'\n",
    "                + df['description'].str.slice(2,5)\n",
    "                )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "id": "dominant-crazy",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['description'] = 'freight charges from distributor for ' + df['description'].str.slice(0,5) + + df['description'].str.lower().str.slice(5,7)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "id": "raised-newfoundland",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = df.groupby(['description', 'catalog_number'], as_index=False).sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "id": "terminal-marsh",
   "metadata": {},
   "outputs": [],
   "source": [
    "        df['vendor'] = 'Secretly Distribution'\n",
    "        df['expense_type'] = 'Recoupable'\n",
    "        df['item_type'] = 'Fee'\n",
    "        df['artist_name'] = ''\n",
    "        df['date'] = ''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "id": "tutorial-windows",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = df[['catalog_number', 'net', 'date', 'vendor', 'expense_type', 'item_type', 'artist_name', 'description']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "id": "applicable-transcription",
   "metadata": {},
   "outputs": [],
   "source": [
    "    df.to_csv('freight-out.csv', index=False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "yellow-clinic",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
