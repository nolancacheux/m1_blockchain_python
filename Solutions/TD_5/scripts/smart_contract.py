from certificate import Certificate

class SmartContractDefinition(Certificate):
    
    # A smart contract definition is a certificates that contains...
    def __init__(self, issuerPublicKey, sourceCode):
        super().__init__(issuerPublicKey)   # ...everything that any certificate has
        self.sourceCode = sourceCode        # ...a source code in the form of a string
        
    # Add the source code to the payload
    def build_payload(self):
        payload = super().build_payload()
        payload['sourceCode'] = self.sourceCode
        return payload
    
    # Add the source code to the displayed dictionary
    def display(self):
        output = super().display()
        output['sourceCode'] = self.sourceCode
        return output
    
    # To generate an instance of the contract, we execute the source code and create an instance using the constructor
    def instantiate_contract(self):
        exec(self.sourceCode)
        return locals()['SmartContract'](self.issuerPublicKey)
    
    # Getting the current state of a smart contract is equivalent to instantiating it and then
    # apply all writing operations found in the blockchain to it.
    @staticmethod
    def get_smart_contract_at_current_state(blockchain, targetSmartContractHash):
        smartContract = None
        writingOperations = []
        for block in blockchain.blockList:
            for certificate in block.certificateList:
                if isinstance(certificate, SmartContractDefinition):
                    smartContractHash = certificate.hash()
                    if smartContractHash == targetSmartContractHash:
                        smartContract = certificate.instantiate_contract()
                if isinstance(certificate, SmartContractWritingOperation):
                    if certificate.targetSmartContractHash == targetSmartContractHash:
                        writingOperations.append(certificate)
        if smartContract is None:
            return
        for op in sorted(writingOperations, key=lambda x: x.timestamp):
            op.apply_on_contract(smartContract)
        return smartContract

class SmartContractWritingOperation(Certificate):
    
    # A smart contract definition is a certificates that contains...
    def __init__(self, issuerPublicKey, targetSmartContractHash, targetFunctionName, functionArgumentList):
        super().__init__(issuerPublicKey)                        # ...everything that any certificate has
        self.targetSmartContractHash = targetSmartContractHash   # ...the target smart contract (its hash)
        self.targetFunctionName = targetFunctionName             # ...the function we want to execute
        self.functionArgumentList = functionArgumentList         # ...and the arguments to pass along
        
    # Again, add everything to the payload
    def build_payload(self):
        payload = super().build_payload()
        payload['targetSmartContractHash'] = self.targetSmartContractHash
        payload['targetFunctionName'] = self.targetFunctionName
        payload['functionArgumentList'] = self.functionArgumentList
        return payload
    
    # Again, add everything to the displayed dictionary
    def display(self):
        output = super().display()
        output['targetSmartContractHash'] = self.targetSmartContractHash
        output['targetFunctionName'] = self.targetFunctionName
        output['functionArgumentList'] = self.functionArgumentList
        return output
    
    # And finally, a function to apply the writing operation to an instantiated contract
    def apply_on_contract(self, smartContract):
        function = getattr(smartContract, self.targetFunctionName)
        argumentList = [self.issuerPublicKey] + self.functionArgumentList
        return function(*argumentList)