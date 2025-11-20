<a name="readme-top"></a>
<div align="center">
	<h1>Spotify 2025 Dashboard</h1>
</div>

<div align="center">
  <img src="https://img.shields.io/github/stars/drod75/SpotifyDataAnalysisDashboard?style=social" alt="GitHub stars"/>
  <img src="https://img.shields.io/github/watchers/drod75/SpotifyDataAnalysisDashboard?style=social" alt="GitHub watchers"/>
  <img src="https://img.shields.io/github/forks/drod75/SpotifyDataAnalysisDashboard?style=social" alt="GitHub forks"/>
</div>

---

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#setup">Setup</a></li>
        <li><a href="#usage">Usage</a></li>
      </ul>
    </li>
    <li><a href="#demo">Demo</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

---

# About The Project

This project aims to create an interactive dashboard using Streamlit to visualize and analyze Spotify music data specifically for the year 2025. The dashboard will showcase trends and popular genres, providing insights into the music landscape of that year.

The data used for this project is sourced from the "Spotify Global Music Dataset (2009-2025)" available on Kaggle. Although the dataset spans multiple years, a Kaggle notebook was utilized to perform Exploratory Data Analysis (EDA) and filter the data to include only entries for 2025, ensuring the dashboard's focus remains on the specified year.

- **Kaggle Dataset:** [Spotify Global Music Dataset (2009-2025)](https://www.kaggle.com/datasets/wardabilal/spotify-global-music-dataset-20092025)
- **Kaggle Notebook (EDA & Data Filtering):** [Spotify 2025 Analysis](https://www.kaggle.com/code/drod75/spotify-2025-analysis/notebook)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Built With

*   <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
*   <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"/>
*   <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/>
*   <img src="https://img.shields.io/badge/Plotly-23F2BC?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly"/>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

Ensure you have Python installed. This project uses `uv` for dependency management and environment setup, but `pip` and `venv` instructions are also provided.

### Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/drod75/SpotifyDataAnalysisDashboard.git
    # OR
    gh repo clone drod75/SpotifyDataAnalysisDashboard
    ```
2.  **Navigate to the project directory:**

    ```bash
    cd SpotifyDataAnalysisDashboard
    ```
3.  **Set up the environment and install dependencies:**

    **Using `uv` (recommended):**

    ```bash
    uv venv
    uv sync
    ```

    **Using `pip` and `venv`:**

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    pip install -r requirements.txt
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Usage

To run the Streamlit dashboard locally:

```bash
streamlit run main.py
```

This will open the dashboard in your web browser.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Demo

A live demo of the dashboard will be available soon. Please check back later!

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact

David Rodriguez - [dr507498@gmail.com](mailto:dr507498@gmail.com) - [LinkedIn](https://www.linkedin.com/in/david-rodriguez-nyc/)

Project Link: [https://github.com/drod75/SpotifyDataAnalysisDashboard](https://github.com/drod75/SpotifyDataAnalysisDashboard)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
