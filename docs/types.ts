// types.ts
export type Environment = 'dev' | 'prod';

export type GitProvider = 'github' | 'gitlab';

export type KubernetesResource =
  | 'Deployment'
  | 'StatefulSet'
  | 'Pod'
  | 'Service'
  | 'PersistentVolumeClaim'
  | 'ConfigMap'
  | 'Secret';

export type KubernetesNamespace = string;

export type DockerImage = string;

export type SshKey = string;

export type AzureResourceGroup = string;