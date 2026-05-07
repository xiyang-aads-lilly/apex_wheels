# see https://github.com/pytorch/pytorch/blob/main/RELEASE.md#release-compatibility-matrix
import yaml

versions = {
    "2.11.0": {"python": [11, 12, 13], "cuda": [130], "deepcompile": 1},
}

cuda_version_mapping = {
    130: "13.0.0",
}

cuda_arch = {
    "13.0.0": "9.0;10.0",
}

pairs_set = set()
pairs = []
for torch_version, pycu in versions.items():
    for python_version in pycu["python"]:
        python_version = f"3.{python_version}"
        for raw_cuda_version in pycu["cuda"]:
            cuda_version = cuda_version_mapping[raw_cuda_version]
            pair = (torch_version, python_version, cuda_version, raw_cuda_version)
            if pair not in pairs_set:
                pairs.append(pair)
                pairs_set.add(pair)

for torch_version, python_version, cuda_version, raw_cuda_version in pairs:
    print(f'- torch-version: "{torch_version}"')
    print(f'  python-version: "{python_version}"')
    print(f'  cuda-version: "{cuda_version}"')
    print(f'  arch: "{cuda_arch[cuda_version]}"')
    # print(f"  deepcompile: {versions[torch_version]['deepcompile']}")

    print(f'  cibw-build: "cp{python_version.replace(".", "")}-*64"')
    print(f'  cibw-build-image: "pytorch/manylinux2_28-builder:cuda{cuda_version[:-2]}"')
    print(f'  cibw-build-cuda-version: "{cuda_version[:-2]}"')
    print(f'  cibw-build-torch-cuda-version: "{raw_cuda_version}"')
    print(f'  cibw-build-cuda-compat-version: "{cuda_version[:-2].replace(".", "-")}"')
