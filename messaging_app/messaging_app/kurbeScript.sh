#!/bin/bash

# Start Minikube
echo "Starting Minikube..."
minikube start

# Verify that the cluster is running
echo "Verifying the cluster is running..."
kubectl cluster-info

# Retrieve the available pods
echo "Retrieving available pods..."
kubectl get pods --all-namespaces
