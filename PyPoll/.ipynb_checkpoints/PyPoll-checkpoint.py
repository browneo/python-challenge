{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv\n",
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid character in identifier (<ipython-input-52-eb889f6be533>, line 66)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-52-eb889f6be533>\"\u001b[0;36m, line \u001b[0;32m66\u001b[0m\n\u001b[0;31m    output_file_path = “election_data_analysis.txt”\u001b[0m\n\u001b[0m                                             ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid character in identifier\n"
     ]
    }
   ],
   "source": [
    "import csv\n",
    "import os\n",
    "\n",
    "\n",
    "pypoll_csv = os.path.join(\"..\", \"Instructions\" , \"PyPoll\", \"Resources\", \"election_data.csv\")\n",
    "\n",
    "with open(pypoll_csv, newline=\"\") as csvfile:\n",
    "    csvreader = csv.reader(csvfile, delimiter=\",\")\n",
    "    csv_header = next(csvreader)\n",
    "    #print(csv_header)\n",
    "   \n",
    " \n",
    "    candidate = []\n",
    "    votes = []\n",
    "    name = []\n",
    "\n",
    "    for row in csvreader:\n",
    "        candidate.append(row[2])\n",
    "    \n",
    "    candidate_count = [[x,candidate.count(x)] for x in set(candidate)]\n",
    "    #print(candidate_coun\n",
    "    \n",
    "    for row in candidate_count:\n",
    "        name.append(row[0])\n",
    "        votes.append(row[1])\n",
    "        \n",
    "    candidate_zip = zip(name, votes)\n",
    "    candidate_lst = list(candidate_zip)\n",
    "    #print(candidate_lst)\n",
    "    \n",
    "    winner = max(votes)\n",
    "    \n",
    "    for row in candidate_lst:\n",
    "        if row[1] == winner:\n",
    "            winner_name = row[0]\n",
    "        #print(winner_name)\n",
    "        \n",
    " #Total number of votes each candidate won       \n",
    "total_votes = len(candidate)\n",
    "\n",
    "tooley_total = candidate.count(\"O'Tooley\")\n",
    "tooley_percent = \"{:.3%}\".format(tooley_total / total_votes)\n",
    "#print(tooley_percent)\n",
    "\n",
    "li_total = candidate.count(\"Li\")\n",
    "li_percent = \"{:.3%}\".format(li_total / total_votes)\n",
    "#print(li_percent)\n",
    "\n",
    "correy_total = candidate.count(\"Correy\")\n",
    "correy_percent = \"{:.3%}\".format(correy_total / total_votes)\n",
    "#print(correy_percent)\n",
    "\n",
    "khan_total = candidate.count(\"Khan\")\n",
    "khan_percent = \"{:.3%}\".format(khan_total / total_votes)\n",
    "\n",
    "\n",
    "print(\"Election Results\")\n",
    "print(\"__________________________\")\n",
    "print(f\"Total Votes: {total_votes}\")\n",
    "print(\"__________________________\")\n",
    "print(f\"O'Tooley: {tooley_percent} ({tooley_total})\")\n",
    "print(f\"Li: {li_percent} ({li_total})\")\n",
    "print(f\"Correy: {correy_percent} ({correy_total})\")\n",
    "print(f\"Khan: {khan_percent} ({khan_total})\")\n",
    "print(\"__________________________\")\n",
    "print(f\"Winner: {winner_name}\")\n",
    "\n",
    "\n",
    "#output file\n",
    "output_file_path = “election_data.txt”\n",
    "    #open file in write mode\n",
    "outFile = open(output_file_path, “w+“)\n",
    "    # function to write output in console and file\n",
    " def printOutput(vLine):\n",
    "     print(vLine)\n",
    "     outFile.write(vLine)\n",
    "     outFile.write(“\\n”)    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
