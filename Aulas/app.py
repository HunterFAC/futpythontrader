{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOaXM8MmJn9KgXLXFKCOPsj",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/HunterFAC/futpythontrader/blob/main/Aula01Streamilit.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cyNeqLEVC4jL",
        "outputId": "8f183cd6-f3a0-493d-8db4-be86245dc673"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m8.1/8.1 MB\u001b[0m \u001b[31m29.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m164.8/164.8 kB\u001b[0m \u001b[31m11.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m188.5/188.5 kB\u001b[0m \u001b[31m12.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m4.7/4.7 MB\u001b[0m \u001b[31m50.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m82.1/82.1 kB\u001b[0m \u001b[31m2.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m62.7/62.7 kB\u001b[0m \u001b[31m2.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m341.8/341.8 kB\u001b[0m \u001b[31m16.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h  Building wheel for validators (setup.py) ... \u001b[?25l\u001b[?25hdone\n"
          ]
        }
      ],
      "source": [
        "! pip install streamlit -q"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st"
      ],
      "metadata": {
        "id": "or4pDNVdDDHo"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import numpy as np"
      ],
      "metadata": {
        "id": "W4SZjYbHDHn_"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "st.title(\"Web App Football Data\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ehOBm7M2DSCh",
        "outputId": "64346fb5-fc8d-4aeb-fadf-aa0b387cd8ec"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "DeltaGenerator()"
            ]
          },
          "metadata": {},
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "st.sidebar.header(\"Leagues\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mat7BGCBDfy4",
        "outputId": "70376c3a-ce57-4cd6-96ec-ffea0b2d1f52"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "DeltaGenerator(_root_container=1, _parent=DeltaGenerator())"
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "selected_league = st.sidebar.selectbox('League', ['England', 'Germany', 'Italy', 'Spain', 'France'])"
      ],
      "metadata": {
        "id": "2Lz0rc6PFUxF"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "st.sidebar.header(\"Season\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HXBC0XshDs3H",
        "outputId": "7218384a-28dd-4bbc-8a30-ef32f56401ef"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "DeltaGenerator(_root_container=1, _parent=DeltaGenerator())"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "selected_season = st.sidebar.selectbox('Season', ['2023/2024', '2022/2023', '2021/2022', '2020/2021'])"
      ],
      "metadata": {
        "id": "KUvpi4ADFvd5"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "WebScreaping Football Data"
      ],
      "metadata": {
        "id": "Du5TpJfeD8xa"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def load_data (league, season):\n",
        "  if selected_league == 'England':\n",
        "    league = 'E0'\n",
        "  if selected_league == 'Germany':\n",
        "    league = 'D1'\n",
        "  if selected_league == 'Italy':\n",
        "    league = 'I1'\n",
        "  if selected_league == 'Spain':\n",
        "    league = 'SP1'\n",
        "  if selected_league == 'France':\n",
        "    league = 'F1'\n",
        "\n",
        "  if selected_season == '2023/2024':\n",
        "    season = '2324'\n",
        "  if selected_season == '2022/2023':\n",
        "    season = '2223'\n",
        "  if selected_season == '2021/2022':\n",
        "    season = '2122'\n",
        "  if selected_season == '2020/2021':\n",
        "    season = '2021'\n",
        "\n",
        "  url = \"https://www.football-data.co.uk/mmz4281/\"+season+\"/\"+league+\".csv\"\n",
        "  data = pd.read_csv (url)\n",
        "  return data"
      ],
      "metadata": {
        "id": "SyMGSDzaEOOV"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df = load_data(selected_league, selected_season)"
      ],
      "metadata": {
        "id": "bbWw0jepE6e1"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "st.subheader('Dataframe: '+selected_league)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4DvkOa-0IsJP",
        "outputId": "2ec280bf-037c-49bb-b836-2721f6ba2342"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "DeltaGenerator()"
            ]
          },
          "metadata": {},
          "execution_count": 18
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "st.dataframe (df)"
      ],
      "metadata": {
        "id": "nzaihEEwI6NZ"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
