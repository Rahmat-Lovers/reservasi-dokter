import hre from "hardhat";
import fs from "fs"

const Contract = await hre.ethers.getContractFactory("Contract");
const contract = await Contract.deploy('0x8626f6940E2eb28930eFb4CeF49B2d1F2C9C1199')

await contract.deployed();

const abi = JSON.parse(fs.readFileSync('./artifacts/contracts/Contract.sol/Contract.json')).abi

fs.writeFileSync('./../abi.json', JSON.stringify(abi))
fs.writeFileSync('./../address.json', JSON.stringify({'address':contract.address}))

console.log(
  "Address: " + contract.address
);
