# About
This project is a test to separe components, where no components can access or dependes directly from another component.

In this example we have 2 components (account and payment) and the app.

## Example
This is a simple example: when an account is created, the system must create a trial subscription too.

## How it works
The usecase `CreateAccountUsecase` (that creates a new account), need to create a trial subscription, and this responsability is from another component `payment`.
To create the subscription, in can follow two ways:
1. The `account` component depends from `payment` component; or
2. The `account` component knows only a interface client, that will be implemented in app and will give access to `payment`, it will be a indirectly dependency.

In this example, I followed the second way.

## Why?
1. This is an experiment
2. If, in the future, the `payment` components goes to another service, and I only will access `payment` using a HTTP interface, I will change only my client implementation.
