import torch
import torch.nn as nn
import torch.optim as optim
import torch.utils.data as thdat

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def np_to_th(x):
    n_samples = len(x)
    return torch.from_numpy(x).to(torch.float).to(DEVICE).reshape(n_samples, -1)


class Net(nn.Module):
    def __init__(
        self,
        input_dim,
        output_dim,
        n_units=100,
        epochs=1000,
        data_loss=nn.MSELoss(),
        lr=1e-3,
        physics_loss=None,
        data_weight=1.0,
        physics_weight=0.1,
    ) -> None:
        super().__init__()

        self.epochs = epochs
        self.data_loss = data_loss
        self.physics_loss = physics_loss
        self.data_weight = data_weight
        self.physics_weight = physics_weight
        self.lr = lr
        self.n_units = n_units

        self.layers = nn.Sequential(
            nn.Linear(input_dim, self.n_units),
            nn.ReLU(),
            nn.Linear(self.n_units, self.n_units),
            nn.ReLU(),
            nn.Linear(self.n_units, self.n_units),
            nn.ReLU(),
            nn.Linear(self.n_units, self.n_units),
            nn.ReLU(),
        )
        self.out = nn.Linear(self.n_units, output_dim)

    def forward(self, x):
        h = self.layers(x)
        out = self.out(h)

        return out

    def fit(self, X, y):
        Xt = np_to_th(X)
        yt = np_to_th(y)

        optimiser = optim.Adam(self.parameters(), lr=self.lr)
        self.train()
        losses = []
        for ep in range(self.epochs):
            optimiser.zero_grad()
            outputs = self.forward(Xt)
            loss = self.data_weight * self.data_loss(yt, outputs)
            if self.physics_loss:
                loss += self.physics_weight * self.physics_loss(self)
            loss.backward()
            optimiser.step()
            losses.append(loss.item())
            if ep % int(self.epochs / 10) == 0:
                print(f"Epoch {ep}/{self.epochs}, loss: {losses[-1]:.2f}")
        return losses

    def predict(self, X):
        self.eval()
        out = self.forward(np_to_th(X))
        return out.detach().cpu().numpy()


class NetDiscovery(Net):
    def __init__(
        self,
        input_dim,
        output_dim,
        n_units=100,
        epochs=1000,
        data_loss=nn.MSELoss(),
        lr=0.001,
        physics_loss=None,
        data_weight=1.0,
        physics_weight=0.1,
    ) -> None:
        super().__init__(
            input_dim, output_dim, n_units, epochs, data_loss, lr,
            physics_loss, data_weight, physics_weight,
        )

        self.kappa = nn.Parameter(data=torch.tensor([0.]))
