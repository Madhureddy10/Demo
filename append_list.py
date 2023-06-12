{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d04b9031",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "enter first name:madhu\n",
      "\n",
      "\n",
      "enter last name:reddy\n",
      "\n",
      "\n",
      "enter first name:qwer\n",
      "\n",
      "\n",
      "enter last name:ks\n",
      "\n",
      "\n",
      "['madhu reddy', 'qwer ks']\n"
     ]
    }
   ],
   "source": [
    "\n",
    "def name(first_name,last_name):\n",
    "    full_name=[]\n",
    "    n=len(first_name)\n",
    "    if (len(first_name)==len(last_name)):        \n",
    "        for i in range(n):\n",
    "                full_name.append(first_name[i]+\" \"+last_name[i])\n",
    "    print(full_name)\n",
    "def append_list():\n",
    "    length=int(input())\n",
    "    first_name=list()\n",
    "    last_name=list()\n",
    "    for i in range(length):\n",
    "        first_name.append(input(\"enter first name:\"))\n",
    "        print(\"\\n\")\n",
    "        last_name.append(input(\"enter last name:\"))\n",
    "        print(\"\\n\")\n",
    "    name(first_name,last_name)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    append_list()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0d32c9fd",
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
