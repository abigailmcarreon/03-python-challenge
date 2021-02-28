{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv\n",
    "import sys\n",
    "\n",
    "election_data_csv = os.path.join (\"PyPoll/Resources/election_data.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'PyPoll/Resources/election_data.csv'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-19-c8f4d5a7f5f8>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mwith\u001b[0m \u001b[0mopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0melection_data_csv\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mnewline\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m\"\"\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mcsvfile\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m     \u001b[0melectionreader\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mcsv\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mreader\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcsvfile\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mdelimiter\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m\",\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m     \u001b[0mcsv_header\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mnext\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0melectionreader\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'PyPoll/Resources/election_data.csv'"
     ]
    }
   ],
   "source": [
    "with open(election_data_csv, newline=\"\") as csvfile:\n",
    "    electionreader = csv.reader(csvfile, delimiter = \",\")\n",
    "\n",
    "    csv_header = next(electionreader)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
