from nilearn import plotting

def plot_brain_image(image_path):
    plotting.plot_stat_map(image_path, title="Brain Activation", threshold=2.0)
    plotting.show()
