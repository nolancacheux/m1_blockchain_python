from certificate import Certificate

class SmartContractDefinition(Certificate):
            
    def __init__(self, issuerPublicKey, sourceCode):
        super().__init__(issuerPublicKey)
        self.sourceCode = sourceCode
        #print(f"Initialized SmartContractDefinition with issuerPublicKey: {issuerPublicKey} and sourceCode: {sourceCode}")
    
    def build_payload(self):
        payload = super().build_payload()
        #print(f"Payload from Certificate: {payload}")
        payload['sourceCode'] = self.sourceCode
        #print(f"Final payload with sourceCode: {payload}")
        return payload
    
    def instantiate_contract(self):
        
        # j'ai un kernel python 3.12.8 pour utiliser locals() 
        
        # Execute the source code in the local namespace
        exec(self.sourceCode)
        
        # Retrieve the SmartContract class from the local namespace
        contract_class = locals()['SmartContract']
        
        # Instantiate the SmartContract class with the issuerPublicKey
        contract_instance = contract_class(self.issuerPublicKey)
        
        # Print the instantiated contract instance
        print(f"Instantiated contract: {contract_instance}")
        
        return contract_instance
    
    @staticmethod
    def get_smart_contract_at_current_state(blockchain, targetSmartContractHash):
        contract_instance = None
        operations = []

        # Traverse the blockchain to find the SmartContractDefinition and collect relevant operations
        for block in blockchain.blockList:
            for certificate in block.certificateList:
                if isinstance(certificate, SmartContractDefinition) and certificate.hash() == targetSmartContractHash:
                    contract_instance = certificate.instantiate_contract()
                elif isinstance(certificate, SmartContractWritingOperation) and certificate.targetSmartContractHash == targetSmartContractHash:
                    operations.append(certificate)

        if contract_instance is None:
            raise ValueError("Smart contract definition not found in the blockchain")

        # Sort operations by timestamp and apply them to the contract instance
        for operation in sorted(operations, key=lambda x: x.timestamp):
            operation.apply_on_contract(contract_instance)

        return contract_instance


class SmartContractWritingOperation(Certificate):
    
    def __init__(self, issuerPublicKey, targetSmartContractHash, targetFunctionName, functionArgumentList):
        super().__init__(issuerPublicKey)
        self.targetSmartContractHash = targetSmartContractHash
        self.targetFunctionName = targetFunctionName
        self.functionArgumentList = functionArgumentList
        #print(f"Initialized SmartContractWritingOperation with issuerPublicKey: {issuerPublicKey}, targetSmartContractHash: {targetSmartContractHash}, targetFunctionName: {targetFunctionName}, functionArgumentList: {functionArgumentList}")
    
    def build_payload(self):
        payload = super().build_payload()
        #print(f"Payload from Certificate: {payload}")
        payload['targetSmartContractHash'] = self.targetSmartContractHash
        payload['targetFunctionName'] = self.targetFunctionName
        payload['functionArgumentList'] = self.functionArgumentList
        #print(f"Final payload with targetSmartContractHash, targetFunctionName, and functionArgumentList: {payload}")
        return payload

    def apply_on_contract(self, contract):
        # Retrieve the function from the contract object
        target_function = getattr(contract, self.targetFunctionName)
        # Execute the function with the provided arguments
        result = target_function(self.issuerPublicKey, *self.functionArgumentList)
        return result
    

