{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP4B5X8IzjwxGDiVy5x9NRY",
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
        "<a href=\"https://colab.research.google.com/github/Ambr0zz/My-Cap-Python-Projects-/blob/main/Copy_of_Project1_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3kWqCsgjPsWw",
        "outputId": "2984aa6a-abcf-4860-a28d-cd2a8ed67b12"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Input the radius of the circle:1.1\n",
            "The area of the  circle with rafius 1.1 is : 3.8013271108436504\n"
          ]
        }
      ],
      "source": [
        "\n",
        "PI =3.141592653589793238\n",
        "r = float(input(\"Input the radius of the circle:\"))\n",
        "area = PI * r * r\n",
        "print(\"The area of the  circle with rafius %.1f\" %r,\"is : %.16f\" %area)"
      ]
    }
  ]
}