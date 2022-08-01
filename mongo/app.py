from bson import ObjectId
from mongo.dbmongo import dbmongo
import hashlib
import jwt

class workbase():
    def __init__(self,obj):
        # print(obj)
        try:
            hash = hashlib.md5()
            hash.update(bytes(obj['password'], 'utf-8'))
        except:
            pass
        #user
        try:
            self.user_id = obj['user_id']
        except:
            pass
        try:
            self.login = obj['login']
        except:
            pass
        try:
            self.password = hash.hexdigest()
        except:
            pass
        try:
            self.name = obj['name']
        except:
            pass
        try:
            self.email = obj['email']
        except:
            pass
        try:
            self.currenttoken = obj['currenttoken']
        except:
            pass
        try:
            self.token = obj['currenttoken']
        except:
            pass

        #provider
        try:
            self.Cnpj = obj['Cnpj']
        except:
            pass
        try:
            self.InscricaoMunicipal=obj['InscricaoMunicipal']
        except:
            pass
        try:
            self.RazaoSocial=obj['RazaoSocial']
        except:
            pass
        #provider
        try:
            self.Municipio = obj['Municipio']
        except:
            pass
        try:
            self.InscricaoMunicipal = obj['InscricaoMunicipal']
        except:
            pass
        try:
            self.NaturezaOperacao = obj['NaturezaOperacao']
        except:
            pass
        try:
            self.RegimeEspecialTributacao = obj['RegimeEspecialTributacao']
        except:
            pass
        try:
            self.OptanteSimplesNacional = obj['OptanteSimplesNacional']
        except:
            pass
        try:
            self.IncentivadorCultural = obj['IncentivadorCultural']
        except:
            pass
        try:
            self.Status = obj['Status']
        except:
            pass 
        try:   
            self.ItemListaServico=obj['ItemListaServico']
        except:
            pass
        try:
            self.Discriminacao=obj['Discriminacao']
        except:
            pass
        try:
            self.QuantidadeRps = obj['QuantidadeRps']
        except:
            pass
        #rps
        try:
            self.NumeroLote = obj['NumeroLote']
        except:
            pass
        try:
            self.Numero = obj['Numero']
        except:
            pass
        try:
            self.Serie = obj['Serie']
        except:
            pass
        try:
            self.Tipo = obj['Tipo']
        except:
            pass
        try:
            self.UltimaNFS = obj['UltimaNFS']
        except:
            pass
        #service
        try:
            self.ValorServicos=obj['ValorServicos']
        except:
            pass
        try:
            self.ValorDeducoes=obj['ValorDeducoes']
        except:
            pass
        try:
            self.ValorPis=obj['ValorPis']
        except:
            pass
        try:    
            self.ValorCofins=obj['ValorCofins']
        except:
            pass
        try:    
            self.ValorInss=obj['ValorInss']
        except:
            pass
        try:    
            self.ValorIr=obj['ValorIr']
        except:
            pass
        try:    
            self.ValorCsll=obj['ValorCsll']
        except:
            pass
        try:    
            self.IssRetido=obj['IssRetido']
        except:
            pass
        try:    
            self.ValorIss=obj['ValorIss']
        except:
            pass
        try:    
            self.ValorIssRetido=obj['ValorIssRetido']
        except:
            pass
        try:    
            self.OutrasRetencoes=obj['OutrasRetencoes']
        except :
            pass    
        try:    
            self.BaseCalculo=obj['BaseCalculo']
        except:
            pass
        try:    
            self.Aliquota=obj['Aliquota']
        except :
            pass    
        try:    
            self.ValorLiquidoNfse=obj['ValorLiquidoNfse']
        except:
            pass
        try:    
            self.DescontoIncondicionado=obj['DescontoIncondicionado']
        except:
            pass
        try:    
            self.DescontoCondicionado=obj['DescontoCondicionado']
        except:
            pass
        try:    
            self.DataEmissao = obj['DataEmissao']
        except:
            pass
        # borrowers
        try:
            self.CpfCnpj=obj['CpfCnpj']
        except :
            pass    
        try:    
            self.RazaoSocial=obj['RazaoSocial']
        except:
            pass
        try:    
            self.Endereco=obj['Endereco']
        except :
            pass    
        try:    
            self.Numero=obj['Numero']
        except :
            pass    
        try:    
            self.Complemento=obj['Complemento']
        except :
            pass    
        try:    
            self.Bairro=obj['Bairro']
        except :
            pass    
        try:    
            self.CodigoMunicipio=obj['CodigoMunicipio']
        except :
            pass    
        try:    
            self.Uf=obj['Uf']
        except :
            pass    
        try:    
            self.Cep=obj['Cep']
        except :
            pass    
        try:    
            self.Email=obj['Email']
        except:
            pass

    def creatuser(self):
        try:
            value = {'name':self.name,'email':self.email,'login':self.login,'password':self.password,"token":''}
            table = "users"
            query = {'login':value['login']}
            validate = dbmongo().select(table,query)
            if validate == []:
                dbmongo().insert(table,value)
                value['_id'] = str(value['_id'])
                value['password'] = 'registered'
                return {"user":value}, 201
            else:
                return  ({ "message" : 'User already existed' },404)
        except Exception as e:
            return  ({ "message" : 'it was not possible to register User' },404)

    def validateuser(self):
        table = 'users'
        query = {'login':self.login}
        validatelogin = dbmongo().select(table,query)
        if validatelogin == [] or validatelogin[0]['password'] != self.password:
            return ({ "message" : 'This user has not yet been registered or the password is invalid' },404)
        else:
            payload = validatelogin[0]
            payload['password'] = 'registered'
            payload['_id'] = str(payload['_id'])
            key= '1234'
            encoded_jwt = jwt.encode(payload=payload, key=key, algorithm="HS256")
            js = {"_id":ObjectId(payload['_id'])}
            value= {"token":encoded_jwt}
            res = dbmongo().update_by_js(table, js, value)
            # print(res)
            Success = { "token": encoded_jwt, "user": payload }
            return (Success,200)

    def validatetoken(self):
        # print(self)
        try:
            table = 'users'
            query = {'token': self.currenttoken}
            validate = dbmongo().select_one(table,query)
            # print(validate)
            if validate['token'] == self.currenttoken:
                return { "token": 'valid'}
            else:
                return { "token": 'invalid'}
        except Exception as e:
            return { "token": 'invalid'}

    def idselectuser(self):
        try:
            table = "users"
            js = {"login":self.login}
            validate = dbmongo().select(table, js)
            if validate == []:
                return ({ "message" : 'User not registered' },404)
            else:
                validate = validate[0]
                value = { 'name':validate['name'],'email':validate['email'],'login':validate['login'] }
                return ({"user": value}, 201)
        except Exception as e:
            return ({ "message" : 'Unable to query user' }, 404)

    def putuser(self):
        try:
            table = "users"
            value = {'name':self.name,'email':self.email,'login':self.login,'password':self.password}
            query = {"login":self.login}
            validate = dbmongo().select(table,query)
            js = {"_id":ObjectId(validate[0]["_id"])}
            dbmongo().update_by_js(table, js, values = value)
            user = dbmongo().select(table,query)[0]
            user['_id'] = str(user['_id'])
            if user == []:
                return ({'message':f"User do'nt exist, register it using another location: {e}"},404)
            else:
                return ({'user':user},201)
        except Exception as e:
            return ({'message':f"could not find the service id: {e}"},404)
        
    def createservice(self):
        try:
            table="service"
            value = {"ValorServicos":self.ValorServicos,
            "ValorDeducoes":self.ValorDeducoes,
            "ValorPis":self.ValorPis,
            "ValorCofins":self.ValorCofins,
            "ValorInss":self.ValorInss,
            "ValorIr":self.ValorIr,
            "ValorCsll":self.ValorCsll,
            "IssRetido":self.IssRetido,
            "ValorIss":self.ValorIss,
            "ValorIssRetido":self.ValorIssRetido,
            "OutrasRetencoes":self.OutrasRetencoes,
            "BaseCalculo":self.BaseCalculo,
            "Aliquota":self.Aliquota,
            "ValorLiquidoNfse":self.ValorLiquidoNfse,
            "DescontoIncondicionado":self.DescontoIncondicionado,
            "DescontoCondicionado":self.DescontoCondicionado,
            "CpfCnpj":self.CpfCnpj,
            "Numero":self.Numero,
            "token":self.token
            }

            query = {"CpfCnpj":self.CpfCnpj,
            "Numero":self.Numero,
            "token":self.token
            }

            validate = dbmongo().select(table,query)
            if validate == []:
                dbmongo().insert(table,value)
                value['_id'] = str(value['_id'])
                return {"user":value},201
            else:
                return ({'message':f"item already exists, overwrite using another location: {e}"},404)
        except Exception as e:
            return ({'message':f"don't cold created inten: {e}"},404)

    def selectservices(self):
        try:
            table="service"
            query = {"token":self.token}
            validate = dbmongo().select(table,query)
            validate=list(validate)
            for i in validate:
                i['_id'] = str(i['_id'])
            return ({"user":validate},201)
        except Exception as e:
            return ({'message':f"don't cold load services: {e}"},404)

    def putservice(self):
        try:
            table = "service"
            value = {"ValorServicos":self.ValorServicos,
            "ValorDeducoes":self.ValorDeducoes,
            "ValorPis":self.ValorPis,
            "ValorCofins":self.ValorCofins,
            "ValorInss":self.ValorInss,
            "ValorIr":self.ValorIr,
            "ValorCsll":self.ValorCsll,
            "IssRetido":self.IssRetido,
            "ValorIss":self.ValorIss,
            "ValorIssRetido":self.ValorIssRetido,
            "OutrasRetencoes":self.OutrasRetencoes,
            "BaseCalculo":self.BaseCalculo,
            "Aliquota":self.Aliquota,
            "ValorLiquidoNfse":self.ValorLiquidoNfse,
            "DescontoIncondicionado":self.DescontoIncondicionado,
            "DescontoCondicionado":self.DescontoCondicionado,
            "CpfCnpj":self.CpfCnpj,
            "Numero":self.Numero,
            "token":self.token
            }
            # print(value)
            query = {"CpfCnpj":str(self.CpfCnpj),
            "Numero":self.Numero
            }
         
            validate = dbmongo().select(table,query)[0]
            js = {"_id":ObjectId(validate["_id"])}
            dbmongo().update_by_js(table, js, value)
            service = dbmongo().select(table,query)[0]
            service['_id'] = str(service['_id'])
            if service == []:
                return ({'message':f"could not find the service id"}, 404)
            else:
                return ({'service':service},201)
        except Exception as e:
            return ({'message':f"could not find the service id: {e}"},404)

    def createrps(self):
        try:
            table="rps"
            value = {"Numero":self.Numero,
            "Serie":self.Serie,
            "Tipo":self.Tipo,
            "UltimaNFS":self.UltimaNFS,
            "NumeroLote":self.NumeroLote,
            "token":self.token
            }

            query = {"Numero":self.Numero,
            "token":self.token
            }

            validate = dbmongo().select(table,query)
            if validate == []:
                dbmongo().insert(table,value)
                value['_id'] = str(value['_id'])
                return {"user":value},201
            else:
                return ({'message':f"item already exists, overwrite using another location: {e}"},404)
        except Exception as e:
            return ({'message':f"don't cold created inten: {e}"},404)

    def selectrps(self):
        try:
            table="rps"
            query = {"token":self.token}
            validate = dbmongo().select(table,query)
            validate=list(validate)
            for i in validate:
                i['_id'] = str(i['_id'])
            return ({"rps":validate},201)
        except Exception as e:
            return ({'message':f"don't cold load rps: {e}"},404)

    def putrps(self):
        try:
            table = "rps"
            value = {"Numero":self.Numero,
            "Serie":self.Serie,
            "Tipo":self.Tipo,
            "UltimaNFS":self.UltimaNFS,
            "NumeroLote":self.NumeroLote,
            "token":self.token
            }

            query = {"Numero":self.CpfCnpj,
            "token":self.token
            }

            validate = dbmongo().select(table,query)[0]
            js = {"_id":ObjectId(validate["_id"])}
            dbmongo().update_by_js(table, js, value)
            rps = dbmongo().select(table,query)[0]
            rps['_id'] = str(rps['_id'])
            if rps == []:
                return ({'message':f"could not find the rps id"}, 404)
            else:
                return ({'rps':rps},201)
        except Exception as e:
            return ({'message':f"could not find the rps id: {e}"},404)

    def createproviders(self):
        try:
            table="providers"
            value = {"Cnpj":self.Cnpj,
            "InscricaoMunicipal":self.InscricaoMunicipal,
            "RazaoSocial":self.RazaoSocial,
            "ItemListaServico":self.ItemListaServico,
            "CodigoMunicipio":self.CodigoMunicipio,
            "Discriminacao":self.Discriminacao, 
            "Municipio":self.Municipio,
            "IncentivadorCultural":self.IncentivadorCultural,
            "NaturezaOperacao":self.NaturezaOperacao,
            "OptanteSimplesNacional":self.OptanteSimplesNacional,
            "RegimeEspecialTributacao":self.RegimeEspecialTributacao,
            "Status":self.Status,
            "token":self.token
            }

            query = {"Cnpj":self.Cnpj}

            validate = dbmongo().select(table,query)
            if validate == []:
                dbmongo().insert(table,value)
                value['_id'] = str(value['_id'])
                return ({"user":value},201)
            else:
                return ({'message':f"item already exists, overwrite using another location: {e}"},404)
        except Exception as e:
            return ({'message':f"item already exists, overwrite using another location: {e}"},404)

    def selectproviders(self):
        try:
            table="providers"
            query = {"token":self.token}
            validate = dbmongo().select(table,query)
            validate=list(validate)
            for i in validate:
                i['_id'] = str(i['_id'])
            return ({"providers":validate},201)
        except Exception as e:
            return ({'message':f"don't cold load providers: {e}"},404)

    def putproviders(self):
        try:
            table = "providers"

            value = {"Cnpj":self.Cnpj,
            "InscricaoMunicipal":self.InscricaoMunicipal,
            "RazaoSocial":self.RazaoSocial,
            "ItemListaServico":self.ItemListaServico,
            "CodigoMunicipio":self.CodigoMunicipio,
            "Discriminacao":self.Discriminacao,
            "Municipio":self.Municipio,
            "IncentivadorCultural":self.IncentivadorCultural,
            "NaturezaOperacao":self.NaturezaOperacao,
            "OptanteSimplesNacional":self.OptanteSimplesNacional,
            "RegimeEspecialTributacao":self.RegimeEspecialTributacao,
            "Status":self.Status,
            "token":self.token
            }

            query = {"Cnpj":self.Cnpj}
            validate = dbmongo().select(table,query)
            js = {"_id":ObjectId(validate[0]["_id"])}
            dbmongo().update_by_js(table, js, values = value)
            providers = dbmongo().select(table,query)[0]
            providers['_id'] = str(providers['_id'])
            if providers == []:
                return ({'message':f"could not find the providers id"}, 404)
            else:
                return ({'providers':providers},201)
        except Exception as e:
            return ({'message':f"could not find the providers id: {e}"},404)

    def createborrowers(self):
        try:
            table="borrowers"
            value = {"CpfCnpj":self.CpfCnpj,
            "RazaoSocial":self.RazaoSocial,
            "Endereco":self.Endereco,
            "Numero":self.Numero,
            "Complemento":self.Complemento,
            "Bairro":self.Bairro,
            "CodigoMunicipio":self.CodigoMunicipio,
            "Uf":self.Uf,
            "Cep":self.Cep,
            "token":self.token
            }

            query = {"CpfCnpj":self.CpfCnpj,
            "token":self.token
            }

            validate = dbmongo().select(table,query)
            if validate == []:
                dbmongo().insert(table,value)
                value['_id'] = str(value['_id'])
                return {"user":value},201
            else:
                return ({'message':f"item already exists, overwrite using another location: {e}"},404)
        except Exception as e:
            return ({'message':f"don't cold created inten: {e}"},404)

    def selectborrowers(self):
        try:
            table="borrowers"
            query = {"token":self.token}
            validate = dbmongo().select(table,query)
            validate=list(validate)
            for i in validate:
                i['_id'] = str(i['_id'])
            return ({"borrowers":validate},201)
        except Exception as e:
            return ({'message':f"don't cold load borrowers: {e}"},404)

    def putborrowers(self):
        try:
            table = "borrowers"

            value = {"CpfCnpj":self.CpfCnpj,
            "RazaoSocial":self.RazaoSocial,
            "Endereco":self.Endereco,
            "Numero":self.Numero,
            "Complemento":self.Complemento,
            "Bairro":self.Bairro,
            "CodigoMunicipio":self.CodigoMunicipio,
            "Uf":self.Uf,
            "Cep":self.Cep,
            "token":self.token
            }

            query = {"Numero":self.Numero,
            "token":self.token
            }

            validate = dbmongo().select(table,query)[0]
            js = {"_id":ObjectId(validate["_id"])}
            dbmongo().update_by_js(table, js, value)
            borrowers = dbmongo().select(table,query)[0]
            borrowers['_id'] = str(borrowers['_id'])
            if borrowers == []:
                return ({'message':f"could not find the borrowers id"}, 404)
            else:
                return ({'borrowers':borrowers},201)
        except Exception as e:
            return ({'message':f"could not find the borrowers id: {e}"},404)


    