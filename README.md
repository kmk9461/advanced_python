
Mission: Our codebase consists of a !.


I. Installation & Set-up 
- packages.py: "header file", contains import statements or functions for handling packages and dependencies required for the project
- utils.py: extra contains utility functions & helper classes
II. Playlist Anayzer
- fetching_spotify_data_unoptimized.ipynb: initial or basic implementations of fetching data from the Spotify API without optimization, serving as a baseline for comparison with optimized versions
- fetching_spotify_data_optimized_base.ipynb: optimization techniques implemented at a base level, still utilizing efficient algorithms or data structures, but offering base architecture w/o excess function overhead, looping, or data transmission
- fetching_spotify_data_optimized_threading.ipynb: optimizing data fetching from Spotify by employing threading techniques, which allow for concurrent execution of tasks
- fetching_spotify_data_optimized_cython.ipynb: This notebook probably demonstrates the optimization of Spotify data fetching using Cython, a superset of Python that allows for writing C extensions, enhancing performance by compiling Python code to C

III. Reccommender 
- spotify_1mil_tracks.ipynb:  working with a dataset of 1 million tracks from Spotify, to suggest relevant tracks 
