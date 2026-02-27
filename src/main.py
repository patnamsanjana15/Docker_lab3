from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

if __name__ == "__main__":
    # Load dataset
    wine = load_wine()
    X, y = wine.data, wine.target

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # Train model
    model = LogisticRegression(max_iter=300)
    model.fit(X_train, y_train)

    # Evaluate model
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    # Save model
    joblib.dump(model, "wine_model.pkl")

    print("Model training completed successfully.")
    print(f"Model accuracy: {acc}")
