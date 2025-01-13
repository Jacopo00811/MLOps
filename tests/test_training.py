from test_project.train import train
import os 

def test_train():
    train(lr=1e-3, batch_size=32, epochs=1)
    assert os.path.exists("models/model.pth")
    assert os.path.exists("reports/figures/training_statistics.png")