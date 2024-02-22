import os
import pysrt

directory = 'transcripts/gbbs'
output_directory = 'transcripts_text/gbbs'  # Define an output directory for the text files

# Create the output directory if it does not exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for season in os.listdir(directory):
    # Check if season is a directory
    if os.path.isdir(os.path.join(directory, season)):
        season_path = os.path.join(output_directory, season)
        # Create a directory for the season in the output directory if it does not exist
        if not os.path.exists(season_path):
            os.makedirs(season_path)
        
        for episode in os.listdir(os.path.join(directory, season)):
            # Check if episode is a directory
            if os.path.isdir(os.path.join(directory, season, episode)):
                episode_path = os.path.join(season_path, episode)
                # Create a directory for the episode in the output directory if it does not exist
                if not os.path.exists(episode_path):
                    os.makedirs(episode_path)
                
                for file in os.listdir(os.path.join(directory, season, episode)):
                    if file.endswith(".srt"):
                        subs = pysrt.open(os.path.join(directory, season, episode, file))
                        # Define the output file path
                        output_file_path = os.path.join(episode_path, f"{os.path.splitext(file)[0]}.txt")
                        with open(output_file_path, 'w', encoding='utf-8') as output_file:
                            for sub in subs:
                                output_file.write(sub.text + '\n')
